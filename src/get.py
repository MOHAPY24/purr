import requests, os, sys, getinfo, getfilesdir, shutil

from colorama import Fore, Style, init
import json

init(autoreset=True)

try:
    PACKAGE = sys.argv[1]
except:
    print(Fore.RED + Style.BRIGHT + f"fatal ERR! " + Style.RESET_ALL + Fore.RESET +  f"No file specified to get.")
    exit(1)


package_files, make, filenames, is_dir = getfilesdir.get_file_list(PACKAGE)
print(Fore.GREEN + Style.BRIGHT + f"info: " + Style.RESET_ALL + Fore.RESET + f"Files to be installed: {len(package_files)}")

if make == True:
    print(Fore.GREEN + Style.BRIGHT + f"info: " + Style.RESET_ALL + Fore.RESET + f"Makefile detected, build will be attempted after installation.")

accept = input("Accept install (Y/n)? ")

if accept.lower() == "y" or accept == "":
    pass
else:
    quit(0)

os.chdir("/etc/purr/builds/")
if os.listdir() != []:
    for f in os.listdir():
        if os.path.isfile(f):
            os.remove(f)
        else:
            shutil.rmtree(f)

os.chdir("../")

CONFIGURE = False
for idx, content in enumerate(package_files):

    if not os.path.exists("/etc/purr/builds/"):
        os.makedirs("/etc/purr/builds/")

    filename = f"/etc/purr/builds/{filenames[idx]}"
    

    if is_dir[idx]:
        os.makedirs(filename, exist_ok=True)
        print(Fore.GREEN + Style.BRIGHT + f"info: " + Style.RESET_ALL + Fore.RESET + f"Created directory '{filename}'.")
        continue
    

    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    print(filename)
    
    with open(filename, "w") as f:
        f.write(content)

    print(filename)
    
    if filename == "/etc/purr/builds/metadata.json":
        print(Fore.GREEN + Style.BRIGHT + f"info: " + Style.RESET_ALL + Fore.RESET + f"Metadata file detected, reading installation info...")
        
        with open("/etc/purr/builds/metadata.json", "r") as f:
            try:
                meta = json.loads(f.read())
                installedin = meta.get("installedin")
                name = meta.get("name", PACKAGE)
                version = meta.get("version")
                author = meta.get("author")
                license = meta.get("license")

            except:
                name = PACKAGE
    else:
        if 'name' not in locals():
            name = PACKAGE

    if filename == "/etc/purr/builds/configure":
        os.chmod(filename, 0o755)
        print(Fore.GREEN + Style.BRIGHT + f"info: " + Style.RESET_ALL + Fore.RESET + f"Set execute permissions for 'configure' script. Are you sure you trust this script?")
        
        if name.lower() == "python":
            print(Fore.YELLOW + Style.BRIGHT + f"WARN! " + Style.RESET_ALL + Fore.RESET + f"Python 'configure' scripts may require additional dependencies to run successfully.")
        CONFIGURE = True  
    print(Fore.GREEN + Style.BRIGHT + f"info: " + Style.RESET_ALL + Fore.RESET + f"Installed file '{filename}' successfully.")

if CONFIGURE:
    if os.path.exists("/etc/purr/builds/") == False:
        os.makedirs("/etc/purr/builds/")
    print(Fore.GREEN + Style.BRIGHT + f"info: " + Style.RESET_ALL + Fore.RESET + f"Running 'configure' script...")
    os.chdir(f"/etc/purr/builds/")
    if name.lower() == "python":
        configure_status = os.system("./configure --prefix=/usr/local")
    else:
        configure_status = os.system("./configure")

    if configure_status != 0:
        print(Fore.RED + Style.BRIGHT + f"fatal ERR! " + Style.RESET_ALL + Fore.RESET + f"'configure' script failed with status code {configure_status}.")
        exit(1)
    os.chdir("../")

if make:
    if os.path.exists("/etc/purr/builds/") == False:
        os.makedirs("/etc/purr/builds/")
    print(Fore.GREEN + Style.BRIGHT + f"info: " + Style.RESET_ALL + Fore.RESET + f"Starting build process using Makefile...")
    os.chdir(f"/etc/purr/builds/")
    make_status = os.system("make")

    if make_status != 0:
        print(Fore.RED + Style.BRIGHT + f"fatal ERR! " + Style.RESET_ALL + Fore.RESET + f"Makefile build failed with status code {make_status}.")
        exit(1)
    os.chdir("../")

print(Fore.GREEN + Style.BRIGHT + f"info: " + Style.RESET_ALL + Fore.RESET + f"All files installed successfully.")

if os.path.exists("/etc/purr/world.json"):
    with open("/etc/purr/world.json", "r") as f:
        try:
            extworld = json.loads(f.read())
        except json.JSONDecodeError:
            extworld = {}
else:
    extworld = {}

with open("/etc/purr/world.json", "w") as f:
    try:
        f.write(json.dumps({**extworld, PACKAGE: {"package": PACKAGE, "installedin" : installedin,"files": filenames, "name": name, "license": license, "author": author, "version": version}}, indent=4) + "\n")
    except NameError:
        print(Fore.YELLOW + Style.BRIGHT + f"WARNING! " + Style.RESET_ALL + Fore.RESET + f"Installation metadata not found, cannot update fully world.json.")
        f.write(json.dumps({**extworld, PACKAGE: {"package": PACKAGE, "files": filenames}}, indent=4) + "\n")

print(Fore.GREEN + Style.BRIGHT + f"info: " + Style.RESET_ALL + Fore.RESET + f"Package '{PACKAGE}' installed successfully.")
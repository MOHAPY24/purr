import os, sys, getfilesdir, shutil
from colorama import Fore, Style, init
import json

try:
    conf = sys.argv[2]
except:
    conf = 'n'

init(autoreset=True)

PACKAGE = "purr"

package_files, make, filenames, is_dir = getfilesdir.get_file_list(PACKAGE)
print(Fore.GREEN + Style.BRIGHT + f"info: " + Style.RESET_ALL + Fore.RESET + f"Files to be installed: {len(package_files)}")

if conf != 'y':
    accept = input("Accept upgrade (Y/n)? ")

    if accept.lower() == "y" or accept == "":
        pass
    else:
        quit(0)

curr_dir = os.curdir
os.chdir("/usr/bin/purr/builds/")
if os.listdir() != []:
    for f in os.listdir():
        if os.path.isfile(f):
            os.remove(f)
        else:
            shutil.rmtree(f)

os.chdir(curr_dir)

for idx, content in enumerate(package_files):

    if not os.path.exists("/usr/bin/purr/builds/"):
        os.makedirs("/usr/bin/purr/builds/")

    filename = f"/usr/bin/purr/builds/{filenames[idx]}"
    
    if is_dir[idx]:
        os.makedirs(filename, exist_ok=True)
        print(Fore.GREEN + Style.BRIGHT + f"info: " + Style.RESET_ALL + Fore.RESET + f"Created directory '{filename}'.")
        continue
    

    os.makedirs(os.path.dirname(filename), exist_ok=True)
        
    with open(filename, "w") as f:
        f.write(content)
    name = PACKAGE

if make:
    if os.path.exists("/usr/bin/purr/builds/") == False:
        os.makedirs("/usr/bin/purr/builds/")
    print(Fore.GREEN + Style.BRIGHT + f"info: " + Style.RESET_ALL + Fore.RESET + f"Starting build process using Makefile...")
    os.chdir(f"/usr/bin/purr/builds/")
    make_status = os.system("make -s")
    



    if make_status != 0:
        print(Fore.RED + Style.BRIGHT + f"fatal ERR! " + Style.RESET_ALL + Fore.RESET + f"Makefile build failed with status code {make_status}.")
        exit(1)
    os.chdir(curr_dir)

print(Fore.GREEN + Style.BRIGHT + f"info: " + Style.RESET_ALL + Fore.RESET + f"All files installed successfully.")
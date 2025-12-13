import json, sys, os
from colorama import Fore, Style, init

init(True)

try:
    PACKAGE = sys.argv[1]
except:
    print(Fore.RED + Style.BRIGHT + f"fatal ERR! " + Style.RESET_ALL + Fore.RESET +  f"No file specified to remove.")
    exit(1)

conf = input("Are you sure you wanna remove said package? (y/N) ")
if conf.lower() == "y":
    pass
else:
    quit(0)

with open("/etc/purr/world.json", 'r') as f:
    world = json.loads(f.read())
    if world[PACKAGE]:
        try:
            install = world[PACKAGE]["installedin"]
        except:
            print(Fore.RED + Style.BRIGHT + f"fatal ERR! " + Style.RESET_ALL + Fore.RESET +  f"Package '{PACKAGE}' doesnt have a full world regestry, cant remove.")
            quit(1)
        remstatus = os.system(f"rm -rf {install}/{PACKAGE}")

        if remstatus != 0:
            print(Fore.RED + Style.BRIGHT + f"fatal ERR! " + Style.RESET_ALL + Fore.RESET +  f"Removal failed with status code {remstatus}")
            quit(1)
    del world[PACKAGE]
with open("/etc/purr/world.json", 'w') as f:
    f.write(json.dumps(world))
print(Fore.GREEN + Style.BRIGHT + f"info: " + Style.RESET_ALL + Fore.RESET + f"Successfully removed package.")

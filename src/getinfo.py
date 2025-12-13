import json

URL = None
try:
    with open("/etc/purr/purr.d/repositories.json", "r") as f:
        config = json.load(f)
        if config["main_stable"]["active"]:
            URL = config["main_stable"]["url"]
        else:
            for key in config:
                if key == "$schema":
                    continue
                if key != "main_stable":
                    if config[key]["active"]:
                        URL = config[key]["url"]
                        break
            if URL is None:
                print("No active configuration found in repositories.json.")
                exit(1)

except FileNotFoundError:
    print("Repositories configuration file not found. maybe rebuild using 'purr rebuildrepos'")
    exit(1)
except json.JSONDecodeError:
    print("Error decoding the configuration file. maybe rebuild using 'purr rebuildrepos'")
    exit(1)

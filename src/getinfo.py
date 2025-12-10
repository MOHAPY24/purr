import json

URL = None
try:
    with open("purr.d/repositories.json", "r") as f:
        config = json.load(f)
        if config["main_stable"]["active"]:
            URL = config["main_stable"]["url"]
        else:
            for key in config:
                if key != "main_stable":
                    if key["active"]:
                        URL = config[key]["url"]
                        break
            if URL is None:
                print("No active configuration found in conf.json.")

except FileNotFoundError:
    print("Repositories configuration file not found.")
except json.JSONDecodeError:
    print("Error decoding the configuration file. maybe rebuid using 'purr rebuildrepos'")

import json
from os.path import exists

config_structure = {
    "key": "",
    "localisation": "",
    "pseudocode-type": ""
}


class Settings:
    __instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(Settings, cls).__new__(cls)
        return cls.__instance

    def __setitem__(self, key, value):
        with open("settings.json", "w+") as file:
            settings = json.load(file)
            settings[key] = value

    @staticmethod
    def init_settings():
        if exists("settings.json"):
            raise FileExistsError
        else:
            with open("settings.json", "w") as file:
                json.dump(config_structure, file, indent=4)




Settings.init_settings()
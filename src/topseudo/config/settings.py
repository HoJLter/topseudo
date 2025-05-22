import json
from os.path import exists




class Settings:
    __instance = None
    __settings_structure = {
        "key": "",
        "localisation": "",
        "pseudocode-type": ""
    }
    _SETTINGS_FILE = "settings.json"

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(Settings, cls).__new__(cls)
        return cls.__instance

    def __getitem__(self, item):
        with open(self._SETTINGS_FILE, "r+") as file:
            settings_data = json.load(file)
            return settings_data[item]

    def __setitem__(self, key, value):
        if key in self.__settings_structure.keys():
            with open(self._SETTINGS_FILE, "r+") as file:
                settings_data = json.load(file)
                file.truncate()
                settings_data[key] = value
                json.dump(settings_data, file, indent=4)
        else:
            raise KeyError

    @classmethod
    def init_settings(cls, overwrite = False):
        if overwrite or not exists(cls._SETTINGS_FILE):
            with open(cls._SETTINGS_FILE, "w") as file:
                json.dump(cls.__settings_structure, file)
        else:
            raise



settings = Settings()
print(settings['pseudocode-type'])



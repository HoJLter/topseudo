import json
from os.path import exists


settings_structure = {
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


    def __init__(self):
        if exists('settings.json'):
            with open("settings.json", 'r+') as file:
                settings_data: dict = json.load(file)
                if not settings_data.values():
                    print("нет значений")
                    json.dump(settings_structure, file)
        else:
            print("нет файла")
            with open("settings.json", 'w') as file:
                json.dump(settings_structure, file)


    @property
    def key(self):
        with open("settings.json", 'r') as file:
            settings_data = json.load(file)
            return settings_data['key']

    @key.setter
    def key(self, value):
        with open("settings.json", 'r+') as file:
            settings_data = json.load(file)
            settings_data['key'] = value


settings = Settings()




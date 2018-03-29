import configparser
import os


# Получение конфига
class Configuration:

    def __init__(self):
        self.config = configparser.RawConfigParser()
        script_dir = os.path.dirname(os.path.abspath(__file__))
        self.config.read('{}/config.ini'.format(script_dir))

    def read_param(self, category, name):
        return self.config.get(category, name)

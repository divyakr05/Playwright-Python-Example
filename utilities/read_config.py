import json
import os


class ConfigurationManager:
    CONFIG_FILE_PATH = os.path.abspath("../config.json")

    @staticmethod
    def get_app_config():
        """ Reads the config.json file."""
        try:
            # Attempt to read from the current directory
            config_data = ConfigurationManager.read_file("config.json")
        except FileNotFoundError:
            # If not found, attempt to read from the absolute path
            config_file_path = ConfigurationManager.CONFIG_FILE_PATH
            config_data = ConfigurationManager.read_file(config_file_path)
        return config_data

    @staticmethod
    def read_file(file_path):
        with open(file_path, 'r') as f:
            file_data = json.load(f)
        return file_data

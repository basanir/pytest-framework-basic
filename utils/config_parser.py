import configparser

class ConfigParser:
    """Class to parse config file"""

    def __init__(self, config_file, env="DEFAULT"):
        """
        Initialize the ConfigParser with a config file.
        """
        self.config = configparser.ConfigParser()
        self.config.read(config_file)
        self.env = env
    
    def get(self, key):
        """
        Get a value from the config file.
        """
        return self.config[self.env][key]
    
    
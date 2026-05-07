class INIConfigParser:
    def __init__(self, file_path):
        self.file_path = file_path
        self.config = {}

    def read_config(self):
        with open(self.file_path, 'r') as file:
            lines = file.readlines()
            section = None
            for line in lines:
                line = line.strip()
                if line.startswith('[') and line.endswith(']'):
                    section = line[1:-1]
                    self.config[section] = {}
                elif '=' in line and section:
                    key, value = line.split('=')
                    self.config[section][key.strip()] = value.strip()

    def get_section(self, section):
        return self.config.get(section)

    def get_value(self, section, key):
        return self.config.get(section, {}).get(key)

    def set_value(self, section, key, value):
        if section not in self.config:
            self.config[section] = {}
        self.config[section][key] = value

    def write_config(self):
        with open(self.file_path, 'w') as file:
            for section in self.config:
                file.write('[' + section + ']\n')
                for key, value in self.config[section].items():
                    file.write(key + '=' + value + '\n')
                file.write('\n')

class ConfigManager:
    def __init__(self, file_path):
        self.parser = INIConfigParser(file_path)

    def load_config(self):
        self.parser.read_config()

    def get_config(self):
        return self.parser.config

    def get_section(self, section):
        return self.parser.get_section(section)

    def get_value(self, section, key):
        return self.parser.get_value(section, key)

    def set_value(self, section, key, value):
        self.parser.set_value(section, key, value)

    def save_config(self):
        self.parser.write_config()

def main():
    config_manager = ConfigManager('config.ini')
    config_manager.load_config()
    print(config_manager.get_config())
    print(config_manager.get_section('section1'))
    print(config_manager.get_value('section1', 'key1'))
    config_manager.set_value('section1', 'key2', 'value2')
    config_manager.save_config()

if __name__ == '__main__':
    main()
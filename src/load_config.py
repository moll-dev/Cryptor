import ConfigParser

config = ConfigParser.ConfigParser()

config.read('cryptor.cfg')

something = config.get('Cryptor Settings', 'APP_KEY')
print something


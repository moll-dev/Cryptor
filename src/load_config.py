import ConfigParser

def load_config(config_file_name):
	settings = {}
	loader = ConfigParser.RawConfigParser()
	try:
		loader.read(config_file_name)
	except:
		print 'Failed to load Cryptor\'s config file'

	sections = loader.sections()
	for section in sections:
		for item in loader.items(section):
			settings[item[0]]=item[1]

	return settings
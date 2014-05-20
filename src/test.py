import cryptorclient
import ConfigParser
from dropbox import session, client, rest


settings = {}
def load_config():
	loader = ConfigParser.RawConfigParser()
	try:
		loader.read('..\\sandbox\\.config\\cryptor.cfg')
		print 'Loaded config file'
	except:
		print 'Failed to load Cryptor\'s config file'

	sections = loader.sections()
	for section in sections:
		for item in loader.items(section):
			settings[item[0]]=item[1]

	return settings

settings = load_config()

cclient = cryptorclient.CryptorClient(settings)
#cclient.(open('SecondTest.txt.crypto'))


#generate_gpg_key('E:\Programming\Cryptor\Secrets')

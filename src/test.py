import cryptorclient
import ConfigParser
from dropbox import session, client, rest


settings = {}
def load_config():
	loader = ConfigParser.RawConfigParser()
	try:
		loader.read('E:\Cryptor\.config\cryptor.cfg')
	except:
		print 'Failed to load Cryptor\'s config file'

	sections = loader.sections()
	for section in sections:
		for item in loader.items(section):
			settings[item[0]]=item[1]

	return settings

settings = load_config()

cclient = cryptorclient.CryptorClient(settings)

flag = True
while(flag):
	#cclient.get_local_delta()
	print cclient.get_remote_delta()

	ans = raw_input('Exit?')
	if ans == 'x':
		flag = False

#generate_gpg_key('E:\Programming\Cryptor\Secrets')

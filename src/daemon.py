import logging, load_config, os
from cryptorclient import CryptorClient

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('Cryptor Daemon')


settings = load_config.load_config('E:\Cryptor\.config\cryptor.cfg')
logger.info('Loaded Config')

client = CryptorClient(settings)
logger.info('Client created successfully')

if client.verify_environment():
	logger.info('Environment is verified')
else:
	logger.info('EXITING: Reason - Environment is not verified')
	exit()

count = 0
flag = True

old_delta = dict ([(f, None) for f in os.listdir (client.normal_dir)])
while(flag):
	delta = dict ([(f, None) for f in os.listdir (client.normal_dir)])
	added = [f for f in delta if not f in old_delta]
	removed = [f for f in old_delta if not f in delta]
	if added:
		for f in added:
			client.push(f)
		print "Added: ", ", ".join (added)

  	if removed:
		for f in removed:
			client.delete(f)
		print "Removed: ", ", ".join (removed)
	old_delta = delta

	ans = raw_input('Exit?')
	if ans == 'x':
		flag = False

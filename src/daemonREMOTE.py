import logging, load_config, pprint
from cryptorclient import CryptorClient

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('Cryptor Daemon')


settings = load_config.load_config('..\\sandbox\\.config\\cryptor.cfg')
logger.info('Loaded Config')

client = CryptorClient(settings)
logger.info('Client created successfully')

if client.verify_environment():
	logger.info('Environment is verified')
else:
	logger.info('EXITING: Reason - Environment is not verified')
	exit()

old_delta = client.db.delta(path_prefix='/Cryptor')

count = 0
flag = True
while(flag):
	count+=1
	delta = client.db.delta(old_delta['cursor'], client.settings['db_home'])




	diff = delta['entries']

	if diff:
		for change in diff:
			#Determine if it's an addition, subtraction, amendment

			#If there's a change
			if change[1]:
				logger.info('There\'s been a change')
				logger.info('In File '+change[0].split('/')[-1])
				#Download or Redownload the file
			else:
				logger.info(change[0]+' Was removed')
				#So delete the file locally using path

	else:
		logger.info('No changes')

	ans = raw_input('Exit? (Loop number: '+str(count)+') ')

	if ans == 'x':
		flag = False

	old_delta = delta
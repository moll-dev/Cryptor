import client
from util import *
import dropbox, webbrowser, gnupg, sys, os, json

working_directory = "E:\Programming\Cryptor\sandbox"
#client = client.Client(working_directory)

filename = "TestFile2.txt"

#client.push(filename)

settings = {}

import ConfigParser

config = ConfigParser.RawConfigParser()

APP_KEY = '6gccue9fycfx31b'
APP_SECRET = 'wrtegtt4cu3z05e'

# cryptor_home = raw_input("Please type the directory (default: current directory): ")
# if not cryptor_home.strip():
# 	print 'You didn\'t enter a directory'
# 	cryptor_home = "E:\Programming\Cryptor\sandbox"
#
# gpg_home = raw_input("Please type the directory for Cryptor's GPG Keys (defaults to Cryptor Home): ")
# if not gpg_home.strip():
# 	print 'Using Cryptor Home'
# 	gpg_home = "E:\Programming\Cryptor\sandbox"

# access_type = "dropbox"
# session = dropbox.session.DropboxSession(APP_KEY, APP_SECRET, access_type)
#
# request_token = session.obtain_request_token()
#
# url = session.build_authorize_url(request_token)
# msg = "Opening %s. Please make sure this application is allowed before continuing."
# print msg % url
# webbrowser.open(url)
# raw_input("[Press enter to continue]")
#
# try:
# 	access_token = session.obtain_access_token(request_token)
# except:
# 	print "You didn't authorize Cryptor to use your Dropbox D:"
# 	exit()
#
#
#
# config.add_section('Cryptor Settings')
# config.set('Cryptor Settings', 'CRYPTOR_HOME', cryptor_home)
# config.set('Cryptor Settings', 'GPG_HOME', gpg_home)
# config.set('Cryptor Settings', 'APP_SECRET', APP_SECRET)
# config.set('Cryptor Settings', 'APP_KEY', APP_KEY)
# config.set('Cryptor Settings', 'CLIENT_SECRET', access_token.secret)
# config.set('Cryptor Settings', 'CLIENT_KEY', access_token.key)
#
#
# with open('cryptor.cfg', 'wb') as configfile:
# 	config.write(configfile)



def load_config():

	loader = ConfigParser.RawConfigParser()
	try:
		loader.read('cryptor.cfg')
	except:
		print 'Failed to load Cryptor\'s config file'

	settings = {}
	settings['cryptor_home']=loader.get('Cryptor Settings', 'cryptor_home')
	settings['gpg_home']=loader.get('Cryptor Settings', 'gpg_home')
	settings['APP_SECRET']=loader.get('Cryptor Settings', 'APP_SECRET')
	settings['APP_KEY']=loader.get('Cryptor Settings', 'APP_KEY')
	settings['CLIENT_SECRET']=loader.get('Cryptor Settings', 'CLIENT_SECRET')
	settings['CLIENT_KEY']=loader.get('Cryptor Settings', 'CLIENT_KEY')

	return settings

settings = load_config()
client = client.Client(settings)

f = open('cryptor.cfg', 'r')
client.pull('TestFile.txt')
print 'File downloaded!'
#generate_gpg_key('E:\Programming\Cryptor\Secrets')

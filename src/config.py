
import ConfigParser
from util import *
import dropbox, webbrowser, gnupg, sys, os, json, hashlib, datetime

"""
This script will setup your cryptor.cfg file!
"""

#Test Directory E:\Programming\Cryptor\sandbox

config = ConfigParser.RawConfigParser()
config.add_section('Cryptor Config File')
config.add_section('Settings')
config.add_section('Paths')
config.add_section('Keys')

config.set('Settings', 'access_type', 'dropbox')

#Don't change these! They're for Cryptor's use
APP_KEY = 'juw0mrsj0i9sfhm'
APP_SECRET = 't1lxj5q54d2ptot'

config.set('Keys', 'APP_SECRET', APP_SECRET)
config.set('Keys', 'APP_KEY', APP_KEY)

cryptor_home = raw_input("Please type the directory (default: current directory): ").strip()
if not cryptor_home.strip():
	cryptor_home = os.getcwd()
config.set('Paths', 'CRYPTOR_HOME', cryptor_home+'\\')
print 'Directory set to: '+cryptor_home+'\n'


gpg_home = raw_input("Please type the directory for Cryptor's GPG Keys (defaults to .config): ").strip()
if not gpg_home.strip():
	gpg_home = cryptor_home+'\\.config'
config.set('Paths', 'GPG_HOME', gpg_home)
print 'Directory set to: '+gpg_home+'\n'

db_home = raw_input("Please type the directory for Cryptor to store your files on Dropbox (defaults to root): ").strip()
if not db_home.strip():
	db_home = ''
config.set('Settings', 'db_home', db_home)
print 'Directory set to: '+db_home+'\n'

print 'Generating paths'
normal_folder_path = cryptor_home+'\\normal\\'
config.set('Paths', 'normal_folder_path', normal_folder_path)
hidden_folder_path = cryptor_home+'\\hidden\\'
config.set('Paths', 'hidden_folder_path', hidden_folder_path)
config_folder_path = cryptor_home+'\\.config\\'
config.set('Paths', 'config_folder_path', config_folder_path)


print 'Setting up file structure in '+cryptor_home
if not os.path.exists(normal_folder_path):
	os.makedirs(normal_folder_path)

if not os.path.exists(hidden_folder_path):
	os.makedirs(hidden_folder_path)

if not os.path.exists(config_folder_path):
	os.makedirs(config_folder_path)


access_type = "dropbox"
session = dropbox.session.DropboxSession(APP_KEY, APP_SECRET, access_type)

request_token = session.obtain_request_token()

url = session.build_authorize_url(request_token)
msg = "Opening %s. Please make sure this application is allowed before continuing."
print msg % url
webbrowser.open(url)
raw_input("[Press enter to continue]")

try:
	access_token = session.obtain_access_token(request_token)
except:
	print "Please authenticate Cryptor with your Dropbox account!"
	exit()

config.set('Keys', 'CLIENT_SECRET', access_token.secret)
config.set('Keys', 'CLIENT_KEY', access_token.key)


print 'Making Cryptor\'s GPG keys\n'
gpg = gnupg.GPG(gnupghome=gpg_home)

password = os.urandom(16).encode('hex')
config.set('Keys', 'GPG_KEY', password)

params = {'key_length':"2048",'name_real':"Cryptor",
		  'name_comment':"Secure your files with Cryptor", 'passphrase': password}

input_data = gpg.gen_key_input(**params)
key = gpg.gen_key(input_data)


with open(config_folder_path+'\\cryptor.cfg', 'wb') as configfile:
	config.write(configfile)

print 'Config file created successfully and written to '+config_folder_path
import client
from util import *
from keychain import *

"""Load settings etc"""
console = Debugger(True)

#these settings can be loaded via json
APP_KEY = '6gccue9fycfx31b'
APP_SECRET = 'wrtegtt4cu3z05e'
ACCESS_TYPE = 'dropbox'


keyfile = "keychains/keychain.data"

try:
	keychain = Keychain(keyfile)
except EnvironmentError:
	print "That keychain file does not exist!"
	ans = raw_input("Would you like to make one? (Y/n):")
	if ans.upper() == "Y":
		generate_keys(APP_KEY, APP_SECRET)
	else:
		print "Boo you didn't want to make any keys"

print "You have a good key and you're ready to GO!"


"""Create client object"""


"""Listen for File operations"""
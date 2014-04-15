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
	generate_keys(APP_KEY, APP_SECRET)
	print "That keychain file does not exist"



"""Create client object"""


"""Listen for File operations"""
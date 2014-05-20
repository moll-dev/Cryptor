import cryptorclient
from util import *
from keychain import *



'''
CURRENT NON WORKING FILE

WILL BE UPDATED LATER

TRY OUT TEST.PY
'''


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
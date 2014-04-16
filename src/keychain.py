import json

class Keychain():


	def __init__(self, filename):
		try:
			self.keychain_file = open(filename, 'r')
			self.load_keys()
			print self.keychain
		except EnvironmentError:
			raise

	def load_keys(self):
		self.json_raw = json.loads(self.keychain_file.read())
		self.keychain = json.dumps(self.json_raw)

	def validate_keys(self):
		pass
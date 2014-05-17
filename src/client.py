#Client Class that handles files transfers, authentication, and encryption
from util import *
from dropbox import client, rest, session

class Client:
	
	def __init__(self, settings):
		self.settings = settings

		"""Initalize GPG"""
		self.gpg = gnupg.GPG(gnupghome=self.settings['gpg_home'])
		self.working_directory = self.settings['cryptor_home']

		"""Initialize Dropbox"""
		ACCESS_TYPE = 'dropbox'
		sess = session.DropboxSession(self.settings['APP_KEY'], self.settings['APP_SECRET'], ACCESS_TYPE)
		sess.set_token(self.settings['CLIENT_KEY'], self.settings['CLIENT_SECRET'])
		self.db = client.DropboxClient(sess)

	def push(self, filename):
		try:
			file_object = open(filename, 'r')
		except IOError:
			raise

		self.encrypt(file_object)
		self.upload(open(filename+'.crypto' ,'r'))


	def pull(self, filename):
		self.download(filename)
		file_object = open(filename+'.crypto', 'r')
		self.decrypt(file_object)


	def encrypt(self, file_object):
		encrypted_ascii_data = self.gpg.encrypt_file(file_object, 'Cryptor')
		encrypted_file = open(file_object.name+".crypto", "w")
		encrypted_file.write(str(encrypted_ascii_data))


	def decrypt(self, file_object):

		passphrase = raw_input('Enter passphrase:')
		decrypted_ascii_data = self.gpg.decrypt_file(file_object, passphrase=passphrase, always_trust=True)

		decrypted_file = open(file_object.name[:-7], "w")
		decrypted_file.write(str(decrypted_ascii_data))


	def upload(self, file_object):
		self.db.put_file(file.name, file)


	def download(self, filename):
		encrypted_file = open(filename+'.crypto', 'wb')
		with self.db.get_file(filename) as f:
			encrypted_file.write(f.read())



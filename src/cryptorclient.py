#Client Class that handles files transfers, authentication, and encryption
from dropbox import client, session
import gnupg, os

class CryptorClient:
	
	def __init__(self, settings):
		self.settings = settings

		self.gpg = gnupg.GPG(gnupghome=self.settings['gpg_home'])
		self.normal_dir = self.settings['normal_folder_path']
		self.hidden_dir = self.settings['hidden_folder_path']
		self.db_home = self.settings['db_home']+'/'

		sess = session.DropboxSession(self.settings['app_key'], self.settings['app_secret'], 'dropbox')
		sess.set_token(self.settings['client_key'], self.settings['client_secret'])
		self.db = client.DropboxClient(sess)


	def push(self, filename):
		try:
			file_object = open(self.normal_dir+filename, 'rb')
		except IOError:
			raise

		self.encrypt(file_object)

		try:
			encrypted_file_object = open(self.hidden_dir+filename+'.crypto' ,'rb')
		except IOError:
			raise

		self.upload(encrypted_file_object)

		file_object.close()
		encrypted_file_object.close()


	def pull(self, filename):
		self.download(filename+'.crypto')
		encrypted_file_object = open(self.hidden_dir+filename+'.crypto', 'rb')
		self.decrypt(encrypted_file_object)


	def encrypt(self, file_object):
		name = file_object.name.split('\\')[-1]
		file_path = self.hidden_dir+name+'.crypto'
		self.gpg.encrypt_file(file_object, 'Cryptor', always_trust=True, output=file_path)


	def decrypt(self, file_object):
		name = file_object.name.split('\\')[-1]
		passphrase = self.settings['gpg_key']
		self.gpg.decrypt_file(file_object, passphrase=passphrase, always_trust=True, output=self.normal_dir+name[:-7])


	def upload(self, file_object):
		name = file_object.name.split('\\')[-1]
		self.db.put_file(self.db_home+name, file_object, overwrite=True)


	def download(self, filename):
		encrypted_file = open(self.hidden_dir+filename, 'wb')
		with self.db.get_file(self.db_home+filename) as f:
			encrypted_file.write(f.read())
		encrypted_file.close()


	def delete_local(self, filename):
		os.remove(self.normal_dir+filename)
		os.remove(self.hidden_dir+filename+'.crypto')

	def delete_remote(self, filename):
		self.db.file_delete(self.db_home+filename+'.crypto')

	def delete(self, filename):
		self.delete_remote(filename)
		os.remove(self.hidden_dir+filename+'.crypto')

	def verify_environment(self):
		if not os.path.isdir(self.normal_dir):
			return False
		if not os.path.isdir(self.hidden_dir):
			return False
		if not os.path.isdir(self.settings['gpg_home']):
			return False
		return True
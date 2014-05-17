import dropbox, webbrowser, gnupg, sys, os, json

def generate_keys(key, secret, gpg_size=2048, key_space="", filename="keychain.data"):

    dropbox_key = generate_client_key(key, secret)
    gpg_key = generate_gpg_key(os.getcwd()+key_space)

    token_file = open(os.getcwd()+key_space+'/'+filename,'w')
    
    keys = {'client_key': dropbox_key.key, 'client_secret': dropbox_key.secret,
           'gpg_private': gpg_key['private'],'gpg_public': gpg_key['public']}
    token_file.write(json.dumps(keys))
    token_file.close()
    print("Token Written to file!\n\n")

def generate_client_key(key, secret):
    access_type = "dropbox"
    session = dropbox.session.DropboxSession(key, secret, access_type)

    request_token = session.obtain_request_token()

    url = session.build_authorize_url(request_token)
    msg = "Opening %s. Please make sure this application is allowed before continuing."
    print msg % url 
    webbrowser.open(url)
    raw_input("[Press enter to continue]")
    access_token = session.obtain_access_token(request_token)

    return access_token

def generate_gpg_key(gpg_home):

    gpg = gnupg.GPG(gnupghome=gpg_home)

    #    input_data = gpg.gen_key_input(key_type="RSA", key_length=gpg_size, )
    """Put asking for key values here!"""
    params = {'key_length':"2048",'name_real':"Cryptor",'passphrase':""}
    #TODO MAKE GETTING PASSWORD MORE SECURE
    params['passphrase'] = raw_input('Enter passphrase: ')
    input_data = gpg.gen_key_input(**params)
    key = gpg.gen_key(input_data)

    return {'private':gpg.export_keys(key.fingerprint, True),'public':gpg.export_keys(key.fingerprint)}


def generate_config():
	"""
	-Working Directory
	-App_Secret *
	-App_Key * Doesn't Change
	-Client_Key
	-Client_Secret
	"""
	cryptor_home = raw_input("Please type the directory (default: current directory): ")
	if cryptor_home is not None:
		cryptor_home = os.getcwd()

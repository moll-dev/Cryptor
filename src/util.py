import dropbox, webbrowser, gnupg

class Debugger():
    def __init__(self, DEBUG_ON=False):
        self.debug = DEBUG_ON

    def log(self, msg):
        if self.debug:
            print "[Debug] "+msg

    def set(self, switch):
        self.debug = switch

def generate_keys(key, secret, gpg_size=2048, key_space="/keychains", filename="keychain.data"):

    #dropbox_key = generate_client_key(key, secret)
    gpg_key = generate_gpg_key(key_space)

    token_file = open(key_space+filename,'w')
    
    #keys = {'client_key': access_token.key, 'client_secret': access_token.secret}
    #token_file.write(json.dumps(keys))
    #token_file.close()
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
    params = {'key_length':"",'name_real':"",'passphrase':""}

    input_data = gpg.gen_key_input(**params)
    key = gpg.gen_key(input_data)

    print key



def debug(msg):
    if DEBUG_ON:
        print(msg)
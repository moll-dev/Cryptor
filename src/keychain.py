class Keychain():
    def __init__(self, filename):
        try:
            self.keychain = open(filename, 'r')

        except EnvironmentError:
            raise
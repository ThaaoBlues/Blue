import keyring


keyring.set_password("test", "username", "password")
print(keyring.get_password("test", "username"))
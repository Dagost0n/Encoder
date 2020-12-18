from cryptography.fernet import Fernet
while True:
    print('What message would you like sent?')
    message = input()
    bmessage = bytes(message, 'utf-8')
    key = Fernet.generate_key()
    print('current key:' + str(key))
    f = Fernet(key)
    token = f.encrypt(bmessage)
    print('encrypted message:' + str(token))
    f.decrypt(token)
    print('message sent:' + str(bmessage))
    print('continue (Y/N)')
    cont = input()
    if (cont == 'Y' or cont == 'y'):
        continue
    else:
        exit()
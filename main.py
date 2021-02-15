import sys
import random
chars = 'abcdefghijklmnopqrstuvwxyz'

def caesar_encrypt(message, key=random.randrange(1, len(chars))):
    chars = 'abcdefghijklmnopqrstuvwxyz'
    cipher_text = ''
    for i in message:
        if i in chars:
            cipher_text += chars[(chars.index(i) + key) % len(chars)]
        else:
            cipher_text += i

    return cipher_text

def brute_force_caesar(message):
    chars = 'abcdefghijklmnopqrstuvwxyz'
    cipher = ''
    text_list = []
    for i in range(len(chars)):
        for j in message:
            if j in chars:
                cipher += chars[(chars.index(j) + i) % len(chars)]
            else:
                cipher += j
        text_list.append(cipher)
        cipher = ''
    
    return text_list

def caesar_decrypt(message, key):
    chars = 'abcdefghijklmnopqrstuvwxyz'
    decipher_text = ''
    for i in message:
        if i in chars:
            decipher_text += chars[(chars.index(i) - key) % len(chars)]
        else:
            decipher_text += i

    return decipher_text


if __name__ == '__main__':
    if sys.argv[1] == '-h':
        print('''
        Venroy Caesar Decoder
        Usage: main.py -[method] {key for decryption and encryption}
        -d: decrypts message 
        -e: encrypts message; if no key is specified, it will select a random key
        -k: decrypts/encrypts message using key
        -b: prints all possible keys
        ''')
    else:
        key = None
        sys.argv.pop(0)
        if sys.argv[-2] == '-k' and sys.argv[1] != '-b':

            key = int(sys.argv[-1])
            sys.argv.pop(-1)
            sys.argv.pop(-1)
            print('key: {}'.format(key))

        method = sys.argv[0]
        sys.argv.pop(0)
        message = ' '.join(sys.argv)
        print('message: ' + message)

        if method == '-d':
            print('message: ' + caesar_decrypt(message, key))
        elif method == '-e':
            if key != None:
                print('secret message: ' + caesar_encrypt(message, key))
            else:
                print('secret message: ' + caesar_encrypt(message))
        elif method == '-b':
            print(brute_force_caesar(message))
from hashlib import sha256
import random
from secret import SECRET_PASSWORD

def make_password(plaintext, app_name):
    salt = get_hexdigest(SECRET_PASSWORD, app_name)[:20]
    hsh = get_hexdigest(salt, plaintext)
    return ''.join((hsh,salt))

def get_hexdigest(salt, plaintext):
    return sha256(b'{salt}{plaintext}').hexdigest()


def password(plaintext, app_name, length=10):
    big_letters = ''.join(list(map(chr,range(65,91))))
    small_letters = big_letters.lower()
    digits = ''.join(list(map(chr,range(48,58))))
    alphabet = (small_letters, big_letters, digits, '!@#$^&*()-_+=~?,.')
    
    hexdigest_text = make_password(plaintext, app_name)
    # convert to int to mix password with new characters
    num = int(hexdigest_text,16) 
    num_chars = len(alphabet)
    
    password = []
    while len(password) < length:
        num, idx = divmod(num,num_chars)
        char = random.choice(alphabet[idx])
        password.append(char)
    return ''.join(password)

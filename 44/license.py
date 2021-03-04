import string
import secrets

alphabet = string.ascii_letters.upper() + string.digits

def gen_key(parts=4, chars_per_part=8):
    password=[]
    for part in range(parts):
        eachPart= ''.join(secrets.choice(alphabet) for i in range(chars_per_part))
        password.append(eachPart) 
    licenseKey='-'.join(password) 
    return licenseKey




import re

def cipher(input):
    res = ""
    for char in input:
        ascii_code = ord(char)
        if ascii_code >= 97 and ascii_code <= 122:
            res += str(219 - ascii_code)
        else:
            res += char
    return res

def decrypt(input):
    return re.sub('[0-9]+', lambda matchObj: chr(int(matchObj.group(0))), input)

sentence = "This is a pen."
crypted = cipher(sentence)
#decrypted = decrypt(crypted)

print("sentence :" + sentence)
print("crypted :" + crypted)
#print("decrypted :" + decrypted)
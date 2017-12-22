import hashlib
input = b'uqwqemis%d'
#input = b'abc%d'

def hashes():
    idx = 0
    while 1:
        h = hashlib.md5(input % idx).hexdigest()
        if h[:5] == '00000':
            yield h[5:7]
        idx += 1

h = hashes()
password = ['_'] * 8
while not all(c.isalnum() for c in password):
    i, c = next(h)
    #print('got [{},{}]'.format(i,c))
    if i.isdigit() and int(i) in range(8) and password[int(i)] == '_':
        password[int(i)] = c
        print(''.join(password))
        

import hashlib
input = b'uqwqemis%d'
#input = b'abc%d'

def hashes():
    idx = 0
    while 1:
        h = hashlib.md5(input % idx).hexdigest()
        if h[:5] == '00000':
            yield h[5]
        idx += 1

h = hashes()
print("Password: ", end='')
for i in range(8):
    print(next(h),end='')

import re
from hashlib import md5

password = "abc"

hashes = {}

def stretch(h):
    for i in range(2016):
        h = md5(h.encode()).hexdigest()
    return h

def gethash(n):
    if n in hashes:
        return hashes[n]
    h = md5(bytes(password + str(n),'utf-8')).hexdigest()
    hashes[n] = stretch(h)
    return hashes[n]

def triple(n):
    h = gethash(n)
    m = re.findall(r'(.)\1\1', h)
    if m:
        return m[0]
    return None

def five(n, c):
    h = gethash(n)
    if re.findall(c + "{5}", h):
        return True
    return False

def iskey(n):
    c = triple(n)
    if c:
        for i in range(1, 1001):
            if five(n + i, c):
                return True
    return False

keys = 0
index = 0
while keys < 64:
    if iskey(index):
        print("key %d: %d" % (keys, index))
        keys += 1
    index += 1

import re
from itertools import chain
# 154, 354, 225 is wrong
insideBrackets = re.compile(r"\[(\w+)\]")

def get_in_out(txt):
    return (insideBrackets.split(txt), insideBrackets.findall(txt))

def get_abas(txt):
    ans = []
    for i in range(len(txt)-2):
        aba = txt[i:i+3]
        if aba[0] == aba[2] and aba[0] != aba[1]:
            ans.append(aba)
    return ans

def all_abas(strs):
    return chain.from_iterable(map(get_abas, strs))

def invert(a):
    return a[1] + a[0] + a[1]
    
def ssl(txt):
    outside, inside = get_in_out(txt)
    outside_abas = set(all_abas(outside))
    inside_abas = set(all_abas(inside))
    
    
with open("input07.txt") as f:
    sslCount = 0
    
    for line in map(str.strip, f):
        if ssl(line):
            sslCount += 1
        
    print("SSL:", sslCount)

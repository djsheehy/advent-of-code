import re

insideBrackets = re.compile(r"\[(\w+)\]")
abba = re.compile(r"(\w)(\w)\2\1")
aba = re.compile(r"(\w)(\w)\1")

def get_in_out(txt):
    return (insideBrackets.split(txt), insideBrackets.findall(txt))

def hasABBA(txt):
    return any(p[0] != p[1] for p in abba.findall(txt))
    
def tls(ip):
    outside, inside = get_in_out(ip)
    if any(hasABBA(s) for s in inside):
        return False
    return any(hasABBA(s) for s in outside)
    
with open("input07.txt") as f:
    tlsCount = 0
    
    for line in map(str.strip, f):
        if tls(line):
            tlsCount += 1
        
    print("TLS:", tlsCount)

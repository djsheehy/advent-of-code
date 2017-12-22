import re

marker = re.compile(r"\((\d+)x(\d+)\)")

def decompress(data):
    #ans = []
    ans = 0
    index = 0
    while index < len(data):
        if data[index] == '(':
            m = marker.search(data, index)
            if m:
                size = int(m.group(1))
                times = int(m.group(2))
                #chunk = data[m.end():m.end()+size]
                #ans.append(chunk * times)
                ans += size * times
                index = m.end()+size
            else:
                #ans.append('(')
                ans += 1
                index += 1
        else:
            #ans.append(data[index])
            ans += 1
            index += 1
    return ans

with open('input09.txt') as f:
    length = 0
    for line in map(str.strip, f):
        length += decompress(line)
    print(length)

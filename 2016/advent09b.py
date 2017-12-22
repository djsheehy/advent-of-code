import re
marker = re.compile(r"\((\d+)x(\d+)\)")

def decode(data):
    #print("decode({})".format(data))
    length = 0
    index = 0
    while index < len(data):
        #print("index:",index)
        if data[index] == '(':
            m = marker.search(data, index)
            size = int(m.group(1))
            times = int(m.group(2))
            chunk = data[m.end():m.end()+size]
            length += decode(chunk) * times
            index = m.end() + size
        else:
            index += 1
            length += 1
    return length

with open('input09.txt') as f:
    print(sum(decode(line) for line in map(str.strip, f)))

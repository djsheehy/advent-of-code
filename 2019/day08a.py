f=open('input08.txt')
data = f.readline().strip()
f.close()
layers = []
for i in range(0, len(data), 150):
    layers.append(data[i:i+150])

mylayer = min(layers, key=lambda l: l.count('0'))
ones = mylayer.count('1')
twos = mylayer.count('2')
print(ones * twos)
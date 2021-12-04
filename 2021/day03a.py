data = [line.strip() for line in open('input03.txt')]
bitcount = [[0,0] for _ in range(12)]

for code in data:
    for i, bit in enumerate(code):
        bit = int(bit)
        bitcount[i][bit] += 1

#print(f"{bitcount=}")
gamma = ['0' if zeros > ones else '1' for zeros, ones in bitcount]
gamma = ''.join(gamma)
#print(f"{gamma=}")
epsilon = ['1' if b == '0' else '0' for b in gamma]
epsilon = ''.join(epsilon)
#print(f"{epsilon=}")
gamma = int(gamma, 2)
epsilon = int(epsilon, 2)
print(gamma * epsilon)
data = [line.strip() for line in open('input03.txt')]

def bitcount(codes, index):
    bc = [0, 0]
    for code in codes:
        bit = int(code[index])
        bc[bit] += 1
    return bc

oxygen = list(data)
for i in range(12):
    bc = bitcount(oxygen, i)
    target_bit = '0' if bc[0] > bc[1] else '1'
    oxygen = [code for code in oxygen if code[i] == target_bit]
    if len(oxygen) == 1:
        oxygen = oxygen[0]
        break

scrubber = list(data)
for i in range(12):
    bc = bitcount(scrubber, i)
    target_bit = '1' if bc[0] > bc[1] else '0'
    scrubber = [code for code in scrubber if code[i] == target_bit]
    if len(scrubber) == 1:
        scrubber = scrubber[0]
        break

print(int(oxygen, 2) * int(scrubber, 2))
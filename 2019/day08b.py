f=open('input08.txt')
data = f.read().strip()
f.close()

# chop up the data into rows of 150
lines = [data[i:i+150] for i in range(0,len(data),150)]
# Start with the first layer
ans = list(lines[0])
# 2's become whatever is on the next layer
for l in lines[1:]:
    for i, pix in enumerate(l):
        if ans[i] == '2':
            ans[i] = pix

# Turn the answer into a rectangle and replace numbers to make it more readable
answer = []
for i in range(0,150,25):
    answer.append(''.join(ans[i:i+25]).replace('0', ' ').replace('1','#'))

print('\n'.join(answer))

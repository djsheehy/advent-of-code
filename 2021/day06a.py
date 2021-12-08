numbers = [int(x) for x in open('input06.txt').read().strip().split(',')]
for day in range(80):
    print(day)
    newfish = 0
    for i in range(len(numbers)):
        if numbers[i] == 0:
            numbers[i] = 6
            newfish += 1
        else:
            numbers[i] -= 1
    numbers.extend([8]*newfish)
    print(len(numbers))

print(len(numbers))
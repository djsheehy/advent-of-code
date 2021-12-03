recipe = '37'
elf1 = 0
elf2 = 1
input = 880751

def step(recipe, e1, e2):
    new = int(recipe[e1]) + int(recipe[e2])
    recipe += str(new)
    e1 = (e1 + int(recipe[e1]) + 1) % len(recipe)
    e2 = (e2 + int(recipe[e2]) + 1) % len(recipe)
    return (recipe, e1, e2)

while(len(recipe) < input+10):
    recipe, elf1, elf2 = step(recipe, elf1, elf2)

print(recipe[input:input+10])
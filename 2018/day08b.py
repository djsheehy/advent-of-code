f=open('input08.txt')
nums = f.read().strip().split()
nums = [int(n) for n in nums]

class Node:
    def __init__(self, children, metadata):
        self.children = children
        self.metadata = metadata
    
    def value(self):
        if not self.children:
            return sum(self.metadata)
        
        v = 0
        for m in self.metadata:
            if m == 0 or m > len(self.children):
                continue
            v += self.children[m-1].value()
        return v
    
def make_tree(iterator):
    child_num = next(iterator)
    meta_num = next(iterator)
    children = []
    metadata = []
    for i in range(child_num):
        children.append(make_tree(iterator))
    for i in range(meta_num):
        metadata.append(next(iterator))
    return Node(children, metadata)

tree = make_tree(iter(nums))
print(tree.value())
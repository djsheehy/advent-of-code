f=open('input08.txt')
nums = f.read().strip().split()
nums = [int(n) for n in nums]

class Node:
    def __init__(self, children, metadata):
        self.children = children
        self.metadata = metadata
    
    def metasum(self):
        ans = sum(self.metadata)
        for n in self.children:
            ans += n.metasum()
        return ans
    
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
print(tree.metasum())
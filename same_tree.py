class TreeNode:
    def __init__(self, x):
        self.val = x
        self.right = None
        self.left = None

# for test
def treeSearch(node, steps):
    if node.left != None:
        treeSearch(node.left, steps)
    steps.append(node.val)
    if node.right != None:
        treeSearch(node.right, steps)

def isSameTree(p, q):
    if p is None and q is None:
        return True

    if p is None or q is None:
        return False

    if isSameTree(p.left, q.left) and isSameTree(p.right, q.right) and (p.val == q.val):
        return True

    return False



p = TreeNode(1)
p.left = TreeNode(2)

q = TreeNode(1)
q.left = TreeNode(2)

print(isSameTree(q, p))

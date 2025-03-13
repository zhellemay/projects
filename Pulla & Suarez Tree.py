class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def swap_level(root, k):
    level = 1
    q = []
    q.append(root)
    while q:
        n = len(q)
        for i in range(n):
            temp = q.pop(0)
            if (level+1) % k == 0:
                temp.left, temp.right = temp.right, temp.left
            if temp.left != None:
                q.append(temp.left)
            if temp.right != None:
                q.append(temp.right)
        level += 1

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.value, end=" ")
        inorder_traversal(root.right)

def preorder_traversal(root):
    if root:
        print(root.value, end=" ")
        preorder_traversal(root.left)
        preorder_traversal(root.right)

def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.value, end=" ")

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
root.left.left = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

k=1

print("Pre-order Traversal")
preorder_traversal(root)
print("\nIn-order Traversal")
inorder_traversal(root)
print("\nPost Order Traversal")
postorder_traversal(root)
print("\n ")

print("Swapping Subtrees...")

swap_level(root, k)

print("\nIn-order Traversal After Swap")
inorder_traversal(root)
print("\nPre-order Traversal After Swap")
preorder_traversal(root)
print("\nPost Order Traversal After Swap")
postorder_traversal(root)


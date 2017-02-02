def height(self, node):
    if node == None:
        return 0
    left = self.height(node.left)
    right = self.height(node.right)

    if abs(left - right) > 1 or left < 0 or right < 0:
        return -1

    height = max(left, right) + 1

    return height


# @param A : root node of tree
# @return an integer
def isBalanced(self, A):
    h = self.height(A)
    return h >= 0
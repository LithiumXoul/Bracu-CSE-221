def get_post_order(n, inorder, preorder):
    if n <= 1: return inorder

    root = preorder[0]
    root_index = None
    for item in inorder:
        if item == root:
            root_index = root
            break

    left_subtree = get_post_order(root_index, inorder[:root_index], preorder[1:root_index + 1])
    right_subtree = get_post_order(n - root_index - 1, inorder[root_index + 1:], preorder[root_index + 1:])

    return left_subtree + right_subtree + [root]

# n = int(input())
# inorder = list(map(int, input().split()))
# preorder = list(map(int, input().split()))

n = 5
inorder = [4, 2, 5, 1, 3]
preorder = [1, 2, 4, 5, 3]

postorder = get_post_order(n, inorder, preorder)
print(" ".join(map(str, postorder)))
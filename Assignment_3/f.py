def post_order(inorder, preorder):
    if len(inorder) <= 1:
        return inorder

    root = preorder[0]
    root_index_in_inorder = None
    for i in range(len(inorder)):
        if inorder[i] == root:
            root_index_in_inorder = i
            break

    lt = post_order(inorder[:root_index_in_inorder], preorder[1:root_index_in_inorder + 1])
    rt = post_order(inorder[root_index_in_inorder + 1:], preorder[root_index_in_inorder + 1:])

    return lt + rt + [root]


import io,os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline


n = int(input())
inorder = list(map(int, input().split()))
preorder = list(map(int, input().split()))

# inorder = [4, 2, 5, 1, 3]
# preorder = [1, 2, 4, 5, 3]

postorder = post_order( inorder, preorder)
print(" ".join(map(str, postorder)))
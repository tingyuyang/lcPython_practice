def BinaryTree(r):
    return [r, [], []]

def insertLeft(root,newBranch):
    print(root)
    t = root.pop(1)
    print (t)
    print("///////")
    if len(t) > 1:
        root.insert(1,[newBranch,t,[]])
    else:
        root.insert(1,[newBranch, [], []])
    return root

r = BinaryTree(3)
insertLeft(r,4)
insertLeft(r,5)

"""
[3, [], []]
[] <- t, len(t) = 0
///////
[3, [4, [], []], []]
[4, [], []] <- t, len(t) = 1
///////
"""

'''What are some potential efficiency disadvantages of having very deep inheritance trees, that is, a large set of classes, A, B, C, and so on, such that B extends A, C extends B, D extends C, etc.?'''

'''The potential efficiency disadvantages of having very deep inheritance trees are:
    1. The time required to look up a method in a deep inheritance tree is proportional to the depth of the tree.

    2. The space required to store a deep inheritance tree is proportional to the depth of the tree.

    If behaior is changes in A wihtout D knowing (ex. diffent teams or people working on it.) then it will be hard to find the bug and very difficult to fix it.

    Also have a larger chance of namespace conflicts that aren't aware of.
    ex. C overrides a function from B that dnowsnt know about it.
'''
'''What are some potential efficiency disadvantages of having very shallow inheritance trees, that is, a large set of classes, A, B, C, and so on, such that all of these classes extend a single class, Z?'''

'''The potential efficiency disadvantages of having very shallow inheritance trees are:
    1. The time required to look up a method in a shallow inheritance tree is proportional to the number of classes in the tree.

    2. The space required to store a shallow inheritance tree is proportional to the number of classes in the tree.

    If any of the classes changes, it will affect all the other classes.
    Namespace conflicts are more likely to occur.
'''
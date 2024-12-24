#Hybrid inheritance
class A:
    pass

class B(A):
    pass        

class C(A):
    pass

class D(B,C):
    pass

#hierarchical inheritance
class A:
    pass

class B(A):
    pass

class C(A):

    pass

class D(B):
    pass
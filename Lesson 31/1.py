class A:
    def __init__(self, a):
        self.a = a
    def __lt__(self, OTHER):
        if self.a < OTHER.a:
            return "Ob1 is less than Ob2"
        else:
            return "Ob1 is not less than Ob2"
    def __gt__(self, OTHER):
        if self.a == OTHER.a:
            return "Both are equal"
        else:
            return "Both are not equal"
ob1 = A(5)
ob2 = A(5)
print("Passed values :", ob1.a, ob2.a)
print(ob1 < ob2)
print(ob1 > ob2)
ob3 = A(3)
ob4 = A(7)
print(ob3 == ob4)
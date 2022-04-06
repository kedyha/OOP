# task_1_oop_1

class Example:
    c = 1
    d = 2
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def func(self):
        self.e = 5
        print(self.e)
    def func1(self):
        return self.c + self.d
    def func2(self):
        return self.a**self.b
ex = Example(int(input()),int(input()))
print(ex.func1())
print(ex.func2())
print(ex.func())
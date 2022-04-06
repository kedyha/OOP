# # task_1_oop_1
#
# class Example:
#     c = 1
#     d = 2
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#     def func(self):
#         self.e = 5
#         print(self.e)
#     def func1(self):
#         return self.c + self.d
#     def func2(self):
#         return self.a**self.b
# ex = Example(int(input()),int(input()))
# print(ex.func1())
# print(ex.func2())
# print(ex.func())


#task_2
#
# class Calc:
#     def __init__(self):
#         self.func4()
#
#     def func(self):
#         return self.a + self.b
#
#     def func1(self):
#         return self.a - self.b
#
#     def func2(self):
#         return self.a * self.b
#
#     def func3(self):
#         if self.b == 0:
#             return "error"
#         else:
#             return self.a/self.b
#
#     def func4(self):
#         self.a = float(input("введите число"))
#         self.b = float(input("введите число"))
#
# while True:
#     print("введите выполняемую операцию: "'+','-','*','/')
#     x = input()
#     ex = Calc()
#     if x == '+':
#         print(ex.func())
#     elif x == '-':
#         print(ex.func1())
#     elif x == '*':
#         print(ex.func2())
#     elif x == '/':
#         print(ex.func3())
#     else:
#         break
#

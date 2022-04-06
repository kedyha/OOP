# # # task_1_oop_1
# #
# # class Example:
# #     c = 1
# #     d = 2
# #     def __init__(self,a,b):
# #         self.a = a
# #         self.b = b
# #     def func(self):
# #         self.e = 5
# #         print(self.e)
# #     def func1(self):
# #         return self.c + self.d
# #     def func2(self):
# #         return self.a**self.b
# # ex = Example(int(input()),int(input()))
# # print(ex.func1())
# # print(ex.func2())
# # print(ex.func())
#
#
# #task_2
# #
# # class Calc:
# #     def __init__(self):
# #         self.func4()
# #
# #     def func(self):
# #         return self.a + self.b
# #
# #     def func1(self):
# #         return self.a - self.b
# #
# #     def func2(self):
# #         return self.a * self.b
# #
# #     def func3(self):
# #         if self.b == 0:
# #             return "error"
# #         else:
# #             return self.a/self.b
# #
# #     def func4(self):
# #         self.a = float(input("введите число"))
# #         self.b = float(input("введите число"))
# #
# # while True:
# #     print("введите выполняемую операцию: "'+','-','*','/')
# #     x = input()
# #     ex = Calc()
# #     if x == '+':
# #         print(ex.func())
# #     elif x == '-':
# #         print(ex.func1())
# #     elif x == '*':
# #         print(ex.func2())
# #     elif x == '/':
# #         print(ex.func3())
# #     else:
# #         break
# #
# # HOME_WORK
#
# class Home:
#     def __init__(self):
#         self.h = 0
#         self.d = 0
#         self.g = 0
#         self.gl = []
#         self.sgl = []
#
#     def func(self, a):
#         if type(a) is str:
#             for i in a:
#                 if i in "aeoiu":
#                     self.h +=1
#                     self.gl.append(i)
#                 else:
#                     self.d +=1
#                     self.sgl.append(i)
#             print("кол гласн",self.h)
#             print("кол согл", self.d)
#             print("длинна слова", self.func1(a))
#             if (self.h * self.d)<= self.func1(a):
#                 print("гласные", self.gl)
#             else:
#                 print("согласные",self.sgl)
#
#         elif type(a) is int:
#             for i in str(a):
#                 i = int(i)
#                 if (i%2) == 0:
#                     self.g += i
#             print("произведение", self.g * self.func1(a))
#
#     def func1(self, a):
#         return len(str(a))
#
#
# ex = Home()
# c = input()
#
# if c.isalpha():
#     ex.func(c)
# elif c.isdigit():
#     ex.func(int(c))
#
#

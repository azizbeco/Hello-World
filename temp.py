# import time

# def find(x ,y):
#     if x<y:
#         for i in range(x,y):
#             print(f"{i} ↧ ")
#             time.sleep(1)
#         # ↧
#     else:
#         for i in range(y,x):
#             print(f"{i}  ↥ ")
#             time.sleep(1)

# find(1,5) 

# x =0

# def count():
#     global x
#     x+=1
#     return x



# print(count())
# print(count())
# print(count())
# print(count())







# def all(x):
#     def count():
#         nonlocal x
#         x+=1
#         return x
#     return count
# counter=all(5)

# print(counter())
# print(counter())
# print(counter())
# print(counter())



# def fibonacci(n):
#     if n<= 0:
#         return 0
#     elif n == 1:
#         return 1
#     return fibonacci(n-1) +fibonacci(n-2)


# print(fibonacci(3))


# def calc():

#     x= input('>>>X ')
#     y= input('>>>Y ')

#     print(int(x)+int(y))
#     result = input('Qayta ishlatish uchun Xisoblash deb yozing ask holda stop ')
#     if result =='stop':
#         return
#     calc()

# calc()



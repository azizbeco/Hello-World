
# def times(n):
#     inner = (lambda x: x * n)
#     return inner

# done = times(2)
# print(done(3))



# inner = (lambda x: x+5)
# print(inner(2))



# def daraja(x):
#     inner = (lambda n:n**x)
#     return inner

# son = daraja(4)

# print(son(2))



# Cache saqlash 

# def cache():
#     saved = {}
#     def get_or_compute(n):
#         if n not in saved:
#             print(f"hisoblaymz {n} uchun .....")
#             saved[n] = n**2

#         return saved[n]
#     return get_or_compute
# cached_square= cache()
# print(cached_square(6))
# print(cached_square(6))


# def factorial(n):
#     if n==1:
#         return 1
#     return n*factorial(n-1)
# print(factorial(5))





#                      Rekursiya

# def find_key(box):
#     for item in box:
#         if isinstance(item,list):
#             print("Karobka ochilyapti.....")
#             if find_key(item):
#                 return True
#             elif item=="kalit":
#                 print("Kalit topildi ")
#                 return True  
#         return False

# big_box=[
#     [],
#     ["daftar","olma",["quti",["kalit"],'olma']]
#     ["daftar",["ruchka",["olma"]]]
# ]


# find_key(big_box)



# Argumentlarni o'zgartirish

# def changer(a,b):
#     a=2
#     b[0]='spam'
# X=1
# L=[1,2]
# changer(X,L)


# print(X,L)


# def changer(a,b):
#     b = b[:] # b.copy()
#     a=2
#     b[0]='spam'
# X=1
# L=[1,2]
# changer(X,L)


# print(X,L)







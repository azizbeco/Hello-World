
# sum=0

# # Ketma ketliklar bilan ishlash
# for x in [1,2,3,4]:
#     sum=sum+x
# print(sum) # forni list bilan ishlashi

# for x in "Javohir":
#     print(sum) # str bilan ishlash

# month =("January","February","March")
# for mo in month:
#     print(mo) # Tuple bilan ishlashi



# player={'name':'Javohir','age':25}

# for key in player:
#     print(value) # dict bilan ishlash 

# for value in player.values(): #player.value() - value ni olib berish uchun
#     print(value)

# for key,value in player.items():
#     print(key)
#     print(value)  # player.items() key va valueni  bir vaqtda olish uchun


# listni aylantirish

# games = ['far cry','assassins','kingdom come','the witcher','fifa']
# for i in range(len(games)):
#     print(games[i])


# list index va value olish 
# games = ['far cry','assassins','kingdom come','the witcher','fifa']
# for index,name in enumerate(games):
#     print(index)
#     print(name)





# import random

# numbers=[]

# while len(numbers) <= 50:
#     random_number=random.randint(1,100)
#     numbers.append(random_number)

# for i in numbers:
#     if i%2:print(i)


# while a<=100:
#     numbers.append(a)
#     a+=1




unli=['a','o','u','i','e']

while True:
    w=input('enter a word: ')
    latters=[]
    for i in w:
        if i in unli:
            latters.append(i)
    print(f"Barcha unli harflar ro'yxati \n{len(latters)}")

    if w=='stop': break



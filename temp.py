
# class Dog:
#     def __init__(self,name,bread): # self- kelajakda yaratiladigon objectga link
#         self.name = name
#         self.bread = bread

# my_dog = Dog('Jek','Bekon')
# print(my_dog.name)
# print(my_dog.bread)

# your_dog = Dog('John','Stake')
# print(your_dog.name)




# class Book:
#     def __init__(self,name,auther,year):
#         self.name = name
#         self.auther = auther
#         self.year = year

# name=input("Book name : ")
# auther=input("Book Auther : ")
# year=input("Book year : ")

# about_book = Book(name,auther,year)

# print(f"{about_book.name} was written  in by {about_book.auther} in {about_book.year}")






# class Dog:
#     def __init__(self,name,bread): # self- kelajakda yaratiladigon objectga link
#         self.name = name  # Yaratiladigon object briktirish
#         self.bread = bread

#     def bark(self,times=1):# yangi object metodini berish
#         for _ in range(times):
#             print(f'{self.name} says Woof!')

# my_dog = Dog('Jek','Bekon')
# print(my_dog.name)
# print(my_dog.bread)

# your_dog = Dog('John','Stake')
# print(your_dog.name)
# my_dog.bark(2)



# class Kvadrat:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y

#     def show(self):

#         if self.x == self.y:
#             return self.x * self.y
#         else:
#             return 2*(self.x + self.y)
        

# while True:
#     x = int(input(">>> "))
#     y = int(input(">>> "))
#     kvadrat = Kvadrat(x,y)

#     print(kvadrat.show())

#     ask=input("yes or no ")
#     if ask=="no":
#         break
#     else:
#         continue



class Character:
    def __init__(self,name,health,power):
        self.name = name
        self.health = health
        self.power = power

    def attack(self,other_character):
        if self.health >0 :
            other_character.health -=self.power
            print(f'{self.name} attack {other_character.name} for {self.power} damaged!')
            if other_character.health <0:
                other_character.health=0
        else:
            print(f'{self.name} is die !')

    def status(self):
        print(f'Character: {self.name}; Health: {self.health}; Power:{self.power}')
    
    def __str__(self):
        print(f'Character: {self.name}; Health: {self.health}; Power:{self.power}')

Hero = Character('Wobahaki',100,14)
Madara = Character('Madara',120,8)

Hero.status()
Hero.attack(Madara)

Madara.status()




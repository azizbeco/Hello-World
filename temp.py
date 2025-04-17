
# class Animal:
#     def speak(self):
#         return "???"
    
# class Dog(Animal):
#     def speak(self):
#         return "Woof"
# class cat(Animal):
#     def  speak(self):
#         return "Meow"

# def animal_sound(animal):
#     print(animal.speak())

# animal_sound(Dog())

# animal_sound(cat())

# animal_sound(Animal())



    
# class Employer:
#     def work(self):
#         return " All "

# class Manager(Employer):
#     def work(self):
#         return "I am Manager"
    
# class Accounter(Employer):
#     def work(self):
#         return "I am Accounter"
#     def travel_time(self, distance):
# class Worker(Employer):
#     def work(self):
#         return "I am worker"


# def employer_method(employer):
#     print(employer.work())


# employer_method(Manager())
# employer_method(Accounter())
# employer_method(Worker())



# class Transport:
#     def travel_time(self,distance):
#         return distance/1
    
# class Bus(Transport):
#     def travel_time(self, distance):
#         return distance/40
# class Bike(Transport):
#     def travel_time(self, distance):
#         return distance/60
    
# class Car(Transport):

#         return distance/100
    
# class Walk(Transport):
#     def __init__(self):
#         return 
    
# print(Bike().travel_time(1000))
# print(Bike().travel_time(1000))
# print(Car().travel_time(1000))
# print(Walk().travel_time(1000))




class Character:
    def __init__(self,name,hp):
        self.name = name
        self.hp = hp
    def attack(self):
        return "Attack"

    def take_damage(self,amount):
        self.hp -= amount
        print(f'{self.name} get {amount} damage. Left {self.hp} HP.')
    def status(self):
        print(f'{self.name} | { self.hp}')

class Warrior(Character):
    def attack(self):
        return f'{self.name} attack with sword and take 20 damage'



class Mage(Character):
    def attack(self):
        return f'{self.name} attack with Mage and take 30 damage'
    


class Archer(Character):
    def attack(self):
        return f'{self.name} attack with Arcch and take 25 damage'



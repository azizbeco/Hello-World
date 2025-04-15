# class Laptop:
#     def __init__(self,name,price,model):
#         self.name = name
#         self.price = price
#         self.model = model
        

#     def discount_price(self,discount):  
#         return self.price - self.price * discount / 100     
# laptop_1 = Laptop('HP',3500000,'Rayzen 5')
# laptop_2 = Laptop('Acer',4000000,'Intel 5')

# laptop_1.discount_price(20)





# class ShoppingCart:
#     def __init__(self):
#         self.__items = [ ]
#     def add_items(self,name,price):
#         self.__items.append({'name':name,'price':price})
#     def remove_items(self,name):
#         for item in self.__items:
#             if item['name'] == name:
#                 self.__items.remove(item)
#                 print('Removed !')
#                 return
                
#         print(f'{name} could not found !')

#     def total_Price(self):
#         return sum(item['price'] for item in self.__items)
    
#     def __str__(self):
#         if not self.__items:
#             return
        
#         cart_lines = ['Basket: ']
#         for item in self.__items:
#             cart_lines.append(f' {item['name']}:{item['price']}')
#         cart_lines.append(f'Total price : {self.total_Price()}$')
#         return '\n'.join(cart_lines)
#     def __repr__(self):
#         return f'ShoppingCart({self.__items})'
    

# User = ShoppingCart()

# User.add_items('Book',100)
# User.add_items('phone',500)
# User.add_items('headphone',250)


# User.remove_items('phone')

# print(User.total_Price())
# print(repr(User))




class BankCard:
    def __init__(self,balance=0):
        self.balance = balance

    def fill_money(self,money):
        self.balance += money

    def withdraw(self,money):
        self.balance -= money

    def card_balance(self):
       return self.balance

Uzcard = BankCard()
Uzcard.fill_money(100)
Uzcard.withdraw(50)
print(Uzcard.card_balance())
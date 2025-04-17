


class Book:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price




class Library:
    def __init__(self):
        self.__items = []

    def add_book(self,book):
        self.__items.append(book)

    def remove_book(self,title):
        for item in self.__items:
            if item['title'] == title:
                self.__items.remove(item)
                print('Removed')
                return
        print(f'{title} could not found !')

    def total_price(self):
        return sum(item['price'] for item in self.__items)

    def __str__(self):

        if not self.__items:
            return

        list_of_book=[' Basket: ']

        for item in self.__items:
            list_of_book.append(f'{item['title']}  {item['author']} ')
        list_of_book.append(f'Total Price:{self.total_price()}$')
        return '\n'.join(list_of_book)

    def search_book(self,author):

        author_list = []

        for item in self.__items:
            if item['author'] == author:
                author_list.append(item)

        for item in author_list:
            print(f' {item['author']} {item['title']} {item['price']}$')


    def sort_by_price(self):
        sort_num = []

        sorted_dict =[]
        for item in self.__items:
            sort_num.append(item['price'])
            sort_num.sort()
        for i in sort_num:
            for item in self.__items:
                if i ==item['price']:
                    sorted_dict.append(item)

        for item in sorted_dict:
            print(f' {item['author']} {item['title']} {item['price']}$')  

        # print(sort_num)
        # print(sorted_dict)


User = Library()

User.add_book(Book('Kichkina shahzoda','Abdulla Qodiriy',500))
User.add_book(Book('Ikki Eshik Orasida','Abdulla Qodiriy',200))
User.add_book(Book('Hayot','Qodiriy',700))

User.remove_book('Hayot')

# User.search_book('Abdulla Qodiriy')
User.sort_by_price()

# User.sort_by_price()
# print(User)
# class of books

class Book:
    def __init__(self, title, author, year) -> None:
        self.title = title
        self.author = author
        self.year = year
    
    def get_info(self) -> str:
        info = f'''
        Book name: {self.title}
        Author: {self.author}
        Year: {self.year}'''
        
        return info

obj1 = Book(title="Harry Porter: Part 1", author="J. K. Rowling", year=2010)
obj2 = Book(title="simpson", author="F. K. Clinton", year=2020)

str1 = obj1.get_info()
str2 = obj2.get_info()

print(str1)
print(str2)

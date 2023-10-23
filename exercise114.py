# Create a class called `Book` with attributes `title`, `author`, and `year`. Implement a method `get_book_info()` that prints the title, author, and year of the book

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year 
    
    def get_book_info(self):
        print(f"{self.title} was written by {self.author} in {self.year}.")
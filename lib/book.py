#!/usr/bin/env python3

class Book:
    def __init__(self):
        self.title = input("Enter the title of the book: ")
        self.page_count = int(input("Enter the number of pages in the book: "))
    
    def page_count(self):
        if self is not None and not isinstance(self, int):
            print("page_count must be an integer")
            return
    
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
        
    
        
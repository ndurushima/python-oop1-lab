#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count
    
    def page_count(self):
        return self._page_count
    
    def page_count(self, value = int):
        if not int:
            print("page_count must be an integer")
        else:
            self._page_count = value
    
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
        
    
        
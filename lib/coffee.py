#!/usr/bin/env python3

class Coffee:
    def __init__(self, size, price = ("Small", "Medium", "Large")):
        self.size = size
        self.price = price
    
    def get_size(self):
        return self._size
    
    def set_size(self, value):
        if value not in ("Small", "Medium", "Large"):
            print("size must be Small, Medium, or Large")
        else:
            self._size = value
    
    def tip(self):
        print("This coffee is great, here`s a tip!")
        self.price += 1

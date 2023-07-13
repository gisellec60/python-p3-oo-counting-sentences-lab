#!/usr/bin/env python3
import re

class MyString:
    
    def __init__(self, value=""):
        self.value = value

    def get_value(self):
        return self._value

    def set_value(self,value):
        if (type(value) == str):
            self._value = value
        else:
            print("The value must be a string.")    
                   
    value=property(get_value, set_value)                

    def is_sentence (self):
          return self.value.endswith(".")
              
    def is_question (self):
           return self.value.endswith("?")    

    def is_exclamation (self):
          return self.value.endswith("!")  

    def count_sentences(self):
        newlist=[]
        if (self.value != 0):
           sentence = re.split('[.!?]', self.value)
           newlist = [x for x in sentence if x != ""]
        return len(newlist)


# simple_string = MyString("This, well, is a sentence. This is too!! And so is this, I think? Woo...")      
# simple_string = MyString("one. two. three?")
# string = MyString()
# string.value=123

MyString("Hello World.").is_sentence() 
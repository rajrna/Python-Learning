"""
import sys

if 5>2:
 print("5 is greater")



#input can be used to get input from user
name = input("What is your name ")
print("hello",name)
print("hello 'friend'") 
print("hello \"friend\"")
print(f"hello, {name}")

#string functions

#strip removes all spaces
name = name.strip()
#capitalize capitalizes the starting letter
name = name.capitalize()
print(f"hello, {name}")

#we can combine both in the same line
# name = name.strip().capitalize()
"""
#main
def main():
    name = input("What is your name ? ")
    hello(name)

def hello(to):
    to = to.strip().title()
    print(f"Hello {to}")
    
main()

    
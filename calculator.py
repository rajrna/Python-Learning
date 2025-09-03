"""
x = input("Enter the first number ")
y = input("Enter the second number ")

#cast the str variables into int variables
z = int(x) + int(y)
print(z)
"""
#you can also cast it during input 
#x = int(input("Enter the first number"))


x= float(input("What is x? "))
y= float(input("What is y? "))
#This one rounds the answer to nearest number
print(f"The answer is {round(x*y)}")
#This one formats the answer 
print(f"The answer is {x*y:.2f}")
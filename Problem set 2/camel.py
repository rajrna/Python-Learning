user_input = input("camelCase : ").strip()
snake = ""
for char in user_input:
    if char.isupper():
        #check if this is the first letter
        if snake:
            snake += "_"
        snake += char.lower()
    else:
        snake += char

print(snake)

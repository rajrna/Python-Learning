import emoji

u_input = input("Input: ").lower()

print(f"Output: {emoji.emojize(u_input,language='alias')}")

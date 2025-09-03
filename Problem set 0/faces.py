#main function that prompts for user input
def main():
    userInput = input("Enter a text with :) or :( : ")
    convert(userInput)

#covert function that replaces emoticons with emojis
def convert(text):
    text = text.replace(":)","🙂").replace(":(","🙁")
    print(f"{text}")

main()

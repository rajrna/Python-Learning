from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
fonts = figlet.getFonts()

def check_args():
    if (sys.argv[1] =="-f"or sys.argv[1]=="--f") and sys.argv[2] in fonts:
        return True

if len(sys.argv)==1:
    u_input = input("Input: ")
    f = random.choice(fonts)
    figlet.setFont(font=f)
elif len(sys.argv )== 3 and check_args():
    u_input = input("Input: ")
    f = sys.argv[2]
    figlet.setFont(font=f)
else:
    sys.exit("Invalid usage")

print(f"Output = ")
print(figlet.renderText(u_input))

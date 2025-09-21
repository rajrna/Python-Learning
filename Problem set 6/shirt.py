import sys
from PIL import Image, ImageOps

def split_ext(f_name):
    return f_name.strip().split(".")
def check_ext(ext_1,ext_2):
    valid_ext = ["jpeg","jpg","png"]
    if (ext_1 in valid_ext) and (ext_2 in valid_ext):
        return True
    else:
        sys.exit("Invalid output")
def check_same_ext(ext_1,ext_2):
    if ext_1 == ext_2:
        return True
    else:
        sys.exit("Input and output have different extensions")

def main():
    if len(sys.argv) != 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) >3:
        sys.exit("Too many command-line arguments")
    try:
        in_file = sys.argv[1]
        out_file = sys.argv[2]
        f_name,f_ext = split_ext(sys.argv[1])
        f_name,s_ext = split_ext(sys.argv[2])
        if check_ext(f_ext,s_ext) and check_same_ext(f_ext,s_ext):
            shirt_img = Image.open("shirt.png")
            in_img = Image.open(in_file)
            cropped_person = ImageOps.fit(in_img, shirt_img.size)
            cropped_person.paste(shirt_img ,(0, 0), shirt_img)
            cropped_person.save(f"{out_file}")
        else:
            sys.exit("File does not exist")
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()

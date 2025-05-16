import os

path = input("enter the directory of the image to convert: ")
is_valid = os.path.isdir(path)
if is_valid == True:
    print("here are the images in the specified directory,", path, "\n")
    print(os.listdir(path))
    original = input("which image would you like to convert? ")
else:
    print("this is not a valid directory. please try again")
    exit
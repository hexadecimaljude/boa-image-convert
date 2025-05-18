import os

# you can add as many formats as you wish
# make sure the formats are in both lower and upper case
# (it's weird i know)

formats = tuple([".png", ".PNG", ".jpg", ".JPG", ".jpeg", ".JPEG", ".heic", ".HEIC", ".gif", ".GIF"])

path = input("Enter the directory of the image to convert: ")

# checks if the path entered is actually an existing/valid path
# if so, the program continues and displays any photos in the directory

is_valid = os.path.isdir(path)
if is_valid == True:
    print("Here are the images in the specified directory,", path, "\n")
    for file in os.listdir(path):
        if (file.endswith(formats)):
            print(file)
    original = input("\nWhich image would you like to convert? ")
else:
    print("This is not a valid directory. Please try again")
    exit
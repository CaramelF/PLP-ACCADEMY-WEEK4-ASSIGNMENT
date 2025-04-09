#reading the file and printing it's contents
try:
    #reading existing file
    filename = input("enter the name of the file you want to read with old content:")
    with open(filename, "r") as file:
        content = file.read()
        print(content) 
#creating and writing a new file
    filename2 = input("enter the name of your new file:")
    new_content = input("share the content you want to add:")
    with open(filename2, 'w') as file:
        mod_file = content + '\n' + new_content
        file.write(mod_file)
    print(f"created successfully {mod_file}")
except FileNotFoundError: 
    print("file not found/error")

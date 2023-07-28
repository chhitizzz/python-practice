# Program to extract the file extension from a given file name

file_name = input("Enter a file name: ")

dot_index = file_name.rfind(".")

if dot_index != -1:
    file_extension = file_name[dot_index + 1:]
    print(f"File extension: {file_extension}")

else:
    print("Invalid file name. No extension found.")
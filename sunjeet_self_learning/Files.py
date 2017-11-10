from sys import argv

script,file_name = argv
print(f"File name input was {file_name}")
# open file for reading 
txt = open(file_name)
# print all the content that has been read
print(txt.read())
print("type the filename again ")
input_prompt = ">:"
# prompt and read the new file name
new_file_name = input(input_prompt)
print(f"the new file name is {new_file_name}")
txt.close()
# if you try to read again after file is closed, reading it again as per below will result in an error
#txt.read()








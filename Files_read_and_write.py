# ~~~~~~~~~read and write example ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from sys import argv

target = open(file_to_erase)
print(target.read())
print (f"""
We're going to erase {file_to_erase}
If you dont that, hit CTRL-C (^C).
If you want that, hit RETURN.
""")
input("?")

print("Opening the file....")
target = open(file_to_erase,'w')

print("Truncating the file")	
target.truncate()

print("NOw let us input somenew lines to write")
line = input("Enter line of text to write to the file")

for i in range (1,100):
    target.write(line)
    target.write("\n")
target.close()

target = open(file_to_erase)
new_file_contents = target.read()
print(f"Check that the new content has been written -----> {new_file_contents}")



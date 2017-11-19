# ~~~~~~~~~read and write example ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# erases content from an existing file , reads new content from command prompt , write to the file , re-reads the file to confirm that new content has been added


from sys import argv

script,file_to_erase = argv

target = open(file_to_erase)
print(target.read())
print (f"""
We're going to erase {file_to_erase}
If you dont that, hit CTRL-C (^C).
otherwise to confirm, hit RETURN.
""")
input("?")

print("Opening the file....")
target = open(file_to_erase,'w')

print("Truncating the file")
target.truncate()

print("NOw let us input somenew lines to write")
line = input("Enter a word to write to the file")

#write that word 100 times in the file 
for i in range (1,100):
    target.write(line)
    target.write("\n")
target.close()

target = open(file_to_erase)
new_file_contents = target.read()
print(f"Check that the new content has been written -----> {new_file_contents}")
target.close()



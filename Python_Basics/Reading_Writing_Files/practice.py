# the file is named f using its path, and the file open mode is mentioned(write mode is selected
# write mode always overwrites the file(prv content is removed, if only one write fn is used)
# append mode keeps the previous content

#with mode automatically closes file no need to do f.close()
with open("///Reading_Writing_Files//funny.txt", "r") as p :
f = open("///Reading_Writing_Files//funny.txt", "a")

f.write("\nI am Confident")  # The statement is written in file "f"
f.close()  # closing a file will free up all the resources that operating system allocates to this file

# f.read(reads the content in the file
# line.split(" ")(when this is used it will splitline(str) wherever space is there into separate words

# f.closed()(prints true or false)

'''
file open modes 
r - reading only(throws error if file doesnt exist)
w - writing only(creates file if doesnt exist,if exists than it will overwrite)
r+ - both reading and writing
w+ - both reading and writing(creates file if doesnt exist, if exists = overwrites)
a -  append mode(whatever we write, file will get appended and existing files do remain)
'''



lst = ["boy", "girl", "man", "woman"]

# print(lst)

for l in lst:
    with open("readWriteToFilePython/writeTestFile.txt", "a") as file:
        file.write(l)
        file.write("\n")


# the above code will save each item in the list on a new line
# this is how the file will look
    # boy
    # girl 
    # man
    # woman


lst = ["boy", "girl", "man", "woman"]

# print(lst)

for l in lst:
    with open("readWriteToFilePython/writeTestFile.txt", "a") as file:
        file.write(l)
        file.write(" ")


# the above code will each item in the list on the same line with a
# space between each word
# this is how the file will look
    # boy girl man woman 
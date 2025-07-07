import  os
# enter inputs in source code only to prevent runtime failures.
fileDirectory = r""  # enter file directory .
changeExtension = "webp"  # enter the extension that will be changed for all except excluded
changedExtension = "png"  # enter the extension that will become new extension for all except excluded
excludedFileExtension = "png"  # enter the file file extension that will remain untouched.
changeNamesList = []  # enter the names for the files without extension if particular names to be given.
listIndexPointer = 0    # used when customised names
for i in os.listdir(fileDirectory):
    print(i)
x = input("do you have customised names(y/n)?")
if x == "y":
    for i in os.listdir(fileDirectory):
        if excludedFileExtension in i:
            os.rename(fileDirectory + "\\" + i,
                      fileDirectory + "\\" + changeNamesList[listIndexPointer] + excludedFileExtension)
            continue
        os.rename(fileDirectory + "\\" + i,
                  fileDirectory + "\\" + changeNamesList[listIndexPointer] + changedExtension)
        listIndexPointer += 1
else:
    for i in os.listdir(fileDirectory):
        if excludedFileExtension in i:

            continue
        os.rename(fileDirectory + "\\" + i,
                  fileDirectory + "\\" + i[:len(i)-len(changeExtension)] + changedExtension)

for i in os.listdir(fileDirectory):
    print(i)

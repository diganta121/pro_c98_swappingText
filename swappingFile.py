
def swapFileData(file1,file2):
    with open(file1,'r') as a:
        dataA = a.read()
    with open(file2,'r') as b:
        dataB = b.read()

    with open(file1,'w') as a:
        a.write(dataB)

    with open(file2,'w') as b:
        b.write(dataA)


fileinp1 = input("enter file1 name : ")
fileinp2 = input("enter file2 name : ")

swapFileData(fileinp1,fileinp2)
print("done")
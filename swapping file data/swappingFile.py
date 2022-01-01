def swapFileData():
    path1 = input("Enter the path of the first file ")
    path2 = input("Enter the path of the second file ")

    file1 = open(path1, 'r')
    file2 = open(path2, 'r')

    data1 = file1.read()
    data2 = file2.read()

    file1.close()
    file2.close()

    file1 = open(path1, 'w')
    file2 = open(path2, 'w')

    file1.writelines(data2)
    file2.writelines(data1)

    file1.close()
    file2.close()

swapFileData()
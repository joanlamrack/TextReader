import re
import glob
import errno

#functions

def searchForTag(file):
    file.seek(0)
    
    topicTagRegex = re.compile(r'#\S+')
    list = re.findall(topicTagRegex, file.read())

    for information in list:
        list[list.index(information)]=information.strip("#")
        
    return list

def searchForTitle(file):
    file.seek(0)
    return file.readline()

def rawcount(file):
    lines = 0
    buf_size = 1024 * 1024
    read_f = file.raw.read

    buf = read_f(buf_size)
    while buf:
        lines += buf.count(b'\n')
        buf = read_f(buf_size)
    return lines

def remover(arrayList, element):
    arrayList.remove(element)
    

#counting lines in the text
def bufcount(file):
    file.seek(0)
    lines = 0
    buf_size = 1024 * 1024
    read_f = file.read # loop optimization

    buf = read_f(buf_size)
    while buf:
        lines += buf.count('\n')
        buf = read_f(buf_size)
    return lines

#for reading the content
def searchForTheContent(file):
    count=bufcount(file)
    file.seek(0)
    i=3
    lines=file.readlines()
    while i<count:
        i=i+1
        print(i)
        if lines[i]=="\n":
            pass
        if lines[i]!="\n":
            print(lines[i])

#main Program starts here
path= '.\\Texts\\*.txt'
files = glob.glob(path)

for name in files:
    file= open(name)

    print(name)
    print(searchForTitle(file))
    print(searchForTag(file))
    file.seek(0)
    print(file.readlines())
    searchForTheContent(file)
    print(bufcount(file))
    
    print("\n\n")

    file.close()

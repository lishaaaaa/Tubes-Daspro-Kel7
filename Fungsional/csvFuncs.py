import os

def lengthFinder(string):           # fungsi untuk mencari panjang suatu string (seperti len())
    length = 0
    for i in string:
        length += 1
    return length

def splitter(string, delimiter):  # pengganti fungsi split() karena gk boleh make split
    split_result = []
    temp = ''
    for x in string:
        if x == delimiter:
            split_result += [temp]
            temp = ''
        else:
            temp += x
    if temp:
        split_result += [temp]
    return split_result
  
  
def csvReader(filename, delimiter=';'):
    with open(filename) as file:
        parse = []
        for line in file:
            values = splitter(line, delimiter)
            parse += [values]
    return parse

def searcher(dicari, sumber):
    found = False
    for i in range(lengthFinder(sumber)):
        if sumber[i] == dicari:
            found = True
            break
    return found



def findMax(dicari):
    max = -9999
    for i in range(lengthFinder(dicari)):
        if dicari[i] >= max:
            max = dicari[i]
    return max

def sortingMerge(list_1, list_2):
    list_3 = []

    while(len(list_1) > 0 and len(list_2) > 0):
        if(list_1[0] > list_2[0]):
            list_3.append(list_2[0])
            del list_2
        
        else:
            list_3.append(list_1[0])
            del list_1

    while( len(list_1) > 0):
        list_3.append(list_1[0])
        del list_1

    while( len(list_2) > 0):
        list_3.append(list_2[0])
        del list_2

    return list_3

def parse(listX):

    if(len(listX) == 1):
        return listX

    parseList_1 = listX[0 : int(len(listX) / 2)]
    parseList_2 = listX[int(len(listX) / 2) : ] 

    parseList_1 = parse(parseList_1) 
    parseList_2 = parse(parseList_2)

    return sortingMerge(parseList_1,parseList_2)

def joined(list1,list2):
    joinedList = list1 + list2 
    return parse(joinedList)

print(joined([1, 4, 5, 8], [2, 3, 6, 7]))

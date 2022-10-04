def merge(list_1, list_2):
    list_3 = []

    while(len(list_1) > 0  and len(list_2) > 0 ):
        if(list_1[0] > list_2[0]):
            list_3.append(list_2[0])
            del list_2[0]
        else:
            list_3.append(list_1[0])
            del list_1[0]
    
    while(len(list_1) > 0):
        list_3.append(list_1[0])
        del list_1[0]

    while(len(list_2) > 0):
        list_3.append(list_2[0])
        del list_2[0]
    
    return list_3

    
def parse(list_x):
    if(len(list_x) == 1):
        return list_x
    
    parseList_1 = list_x[0 : int( len(list_x) / 2) ]
    parseList_2 = list_x[int( len(list_x) / 2)  : ]

    parseList_1 = parse(parseList_1)
    parseList_2 = parse(parseList_2)

    return merge(parseList_1,parseList_2)


print(parse([0,4,5,8,6,9,55,36]))
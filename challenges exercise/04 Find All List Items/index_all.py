def index_all(search_list, item):
    index_list = []
    for index, value in enumerate(search_list):
        if value == item:
            index_list.append([index])
        elif isinstance(search_list[index], list):
            for i in index_all(search_list[index], item):
                index_list.append([index] + i)
    return index_list
#recursion,lists,arrays multi dimensional
#myversion
def index_all2(search_list, item):
    index_list = []#final list
    for index, value in enumerate(search_list):
        if value == item:#equality op any object ex. [1]==[1] or 1==1 than true
            index_list.append([index])#save it
        elif isinstance(search_list[index], list):#check if the instance is a list
            for i in index_all(search_list[index], item):#recursive call if ex. [[],[1,3]...]
                index_list.append([index] + i)#save the returned list if any i matches
                #note here the recursion make the problem easier to approach as we can do this
                #iteratively but it will be a mess to check as we gonna write the same code
                #plus extra lines for each nested level...not the best
    return index_list #return the final lists


# commands used in solution video for reference
if __name__ == '__main__':
    example = [[[1, 2, 3], 2, [1, 3]], [1, 2, 3]]
    print(index_all(example, 2))  # [[0, 0, 1], [0, 1], [1, 1]]
    print(index_all(example, [1, 2, 3]))  # [[0, 0], [1]]

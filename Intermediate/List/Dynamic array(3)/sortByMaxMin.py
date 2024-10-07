def sortByMaxMin(arr):

    arr.sort()
    sortArray = []

    while arr:
        if arr:
            sortArray.append(arr.pop())  
        if arr:
            sortArray.append(arr.pop(0))  
    return sortArray
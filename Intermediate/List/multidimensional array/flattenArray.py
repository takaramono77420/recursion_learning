def flattenArray(arr):
    result = []
    for number in arr:
        if isinstance(number, int):
            if number % 2 == 0:
                result.append(number)
        else:
            result += flattenArray(number)

    return result

print(flattenArray([1,2,3,[4,5,[6,7]],8,[9,10,11],12,13]))
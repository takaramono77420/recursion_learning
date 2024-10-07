def evenRange(a,b):
    # 関数を完成させてください
    array = []

    for i in range(a, b + 1):
        if i % 2 == 0:
            array.append(i)
    
    return array

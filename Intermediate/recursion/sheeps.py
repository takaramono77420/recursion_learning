def sheeps(count):
    # 関数を完成させてください

    if count == 1:
        return "1 sheep ~ "
    
    return sheeps(count - 1)  + str(count) + " sheep ~ "


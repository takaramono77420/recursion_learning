def doYouFail(string):
    # 関数を完成させてください

    count = 0

    for char in string:
        if char == "A":
            count += 1
        
        if count >= 3:
            return "fail"
    
    return "pass"
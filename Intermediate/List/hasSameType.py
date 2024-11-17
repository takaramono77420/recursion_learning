def hasSameType(user1,user2):
    # 関数を完成させてください
    if len(user1) != len(user2):return False

    hashMap = {}

    for index, user1Type in enumerate(user1):
        user2Type = user2[index]

        if user1Type not in hashMap and user2Type not in hashMap.values():
            hashMap[user1Type] = user2Type
        
        if hashMap.get(user1Type) != user2Type:
            return False
    
    return True
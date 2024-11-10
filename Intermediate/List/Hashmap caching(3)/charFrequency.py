def charFrequency(message):
    # 関数を完成させてください

    message = message.replace(' ', '').lower()

    hashmap = {}
    for char in message:
        hashmap[char] = hashmap.get(char, 0) + 1

    return [f"{char} : {count}" for char, count in sorted(hashmap.items())]
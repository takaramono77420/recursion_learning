def hasPenalty(records):
    # 関数を完成させてください
    record_len = len(records)
    for record_i in range(record_len-1):
        if records[record_i] > records[record_i + 1]:
            return True
    
    return False

def rotateByTimes(ids,n):

    ids_len = len(ids)

    n = n % ids_len
    n = ids_len - n

    new_ids = []

    # idsを回転させて新しいリストに追加
    for i in range(ids_len):
        new_ids.append(ids[(n + i) % ids_len])

    return new_ids
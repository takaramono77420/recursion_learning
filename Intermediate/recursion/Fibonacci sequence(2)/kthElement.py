def kthElement(n,k):
    # 関数を完成させてください

    # ベースケース
    if n <= 1:
        return 0
    
    if k % 2 == 1:
        return 0 if kthElement(n - 1, (k + 1) / 2) == 0 else 1
    else:
        return 1 if kthElement(n - 1, k / 2) == 0 else 0
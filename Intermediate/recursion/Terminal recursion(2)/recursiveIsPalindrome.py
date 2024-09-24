def recursiveIsPalindromeHelper(s):
    if len(s) <= 1:
        return True
    
    if s[0] != s[-1]:
        return False  
    
    return recursiveIsPalindromeHelper(s[1:-1])

def recursiveIsPalindrome(s):
    # 関数を完成させてください

    s = s.replace(' ', '')
    s = s.lower()

    return recursiveIsPalindromeHelper(s[1:-1])
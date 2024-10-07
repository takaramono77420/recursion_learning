def validEmailList(emailList):
    # 関数を完成させてください
    correctEmailList = []
    
    for email in emailList:

        if not (not email.find(' ') == -1 or not email.count('@') == 1 or \
            not email[email.find('@')::].find('.') != -1 or not email.find('@') != 0):
            correctEmailList.append(email)
    
    return correctEmailList
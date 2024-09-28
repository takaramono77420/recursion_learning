class Person:
    # 問題文の指定した条件に従って、コンストラクタやメソッドを記述します。
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
    
    def getFullName(self):
        return self.firstName + " " + self.lastName
    
    def getInitial(self):
        return self.firstName[0] + "." + self.lastName[0]
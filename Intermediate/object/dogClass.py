class Dog:
    # 問題文の指定した条件に従って、コンストラクタやメソッドを記述します。
    def __init__(self, name, size, age):
        self.name = name
        self.size = size
        self.age = age
    
    def bark(self):
        if self.size >= 50:
            return "Wooof! Woof!"
        elif self.size >= 20:
            return "Ruff! Ruff!"
        else:
            return "Yip! Yip!"
    
    def calcHumanAge(self):
        return 12 + (self.age - 1) * 7
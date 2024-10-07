class Files:
    def __init__(self, fileName, fileExtension, content, parentFolder):
        self.fileName = fileName
        self.fileExtension = fileExtension
        self.content = content
        self.parentFolder = parentFolder
    
    def getLifetimeBandwidthSize(self):
        size = len(self.content) * 25
        if size >= 1000:
            return str(size * 0.001) + "GB"
        else:
            return str(size) + "MB"


    def prependContent(self, data):
        self.content = data + self.content
        return self.content
    
    def addContent(self, data, position):
        self.content = self.content[:position] + data + self.content[position:]
        return self.content
    
    def showFileLocation(self):
        return self.parentFolder + " > " + self.fileName + self.fileExtension

assignment = Files("assignment", ".word", "ABCDEFGH", "homework")
print(assignment.getLifetimeBandwidthSize())
print(assignment.prependContent("MMM"))
print(assignment.addContent("hello world", 5))
print(assignment.showFileLocation())

blade = Files("blade", ".txt", "bg-primary text-white m-0 p-0 d-flex justify-content-center", "view")
print(blade.getLifetimeBandwidthSize())
print(blade.addContent("font-weight-bold ", 11))
print(blade.showFileLocation())
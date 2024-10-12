class Student:

    def __init__(self, studentId, firstName, lastName, gradeLevel):
        self.studentId = studentId
        self.firstName = firstName
        self.lastName = lastName
        self.gradeLevel = gradeLevel
    
    def getStudentInfo(self):
        return self.studentId + ": " + self.firstName + " " + self.lastName + "(" + str(self.gradeLevel) + "gr)"

class Classroom:

    def __init__(self, students, courseName, teacher):
        self.students = students
        self.courseName = courseName
        self.teacher = teacher
    
    def getClassIdentity(self):
        return self.courseName + " managed by " + self.teacher
    
    def getNumberOfStudents(self):
        return len(self.students)

classroom1 = Classroom([ Student("AC-343424", "James", "Smith", 6),  Student("AC-343428", "Maria", "Garcia", 5), Student("AC-343434", "Robert", "Johnson", 3), Student("AC-343454","Danny", "Robertson",10)], "Algebra II", "Emily Theodore")

print(classroom1.getClassIdentity())

print(classroom1.getNumberOfStudents())


classroom2 = Classroom([ Student("AC-340014","Kent", "Carter",9),  Student("AC-340024","Isaiah", "Chambers",10), Student("AC-340018","Leta", "Ferguson", 7)], "English", "Daniel Pherb")

print(classroom2.getClassIdentity())

print(classroom2.getNumberOfStudents())
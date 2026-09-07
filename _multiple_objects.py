class Student:
    def __init__(self, name, branch):
        self.name = name
        self.branch = branch

    def display(self):
        print(self.name, "-", self.branch)


s1 = Student("Nagasri", "AIML")
s2 = Student("Anu", "CSE")
s3 = Student("Sanjana", "ECE")

s1.display()
s2.display()
s3.display()


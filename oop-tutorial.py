class Student:
    class_grade = "2ha"
    # class attributes defined within the constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # def __str__(self):
    #     return f"The student's name is {self.name}. The student is {self.age}. He already got a class of {self.class_grade}"


    def student_details(self):
        return f"The student's name is {self.name}. The student is {self.age}. He already got a class of {self.class_grade}"

# student_details = Student("George", 28)
# student_details.class_grade = "2la"
# print(student_details)
# print(student_details.student_details())

class PrimaryStudent(Student):
    def student_details(self, color):
        return f"{self.name}'s a primary student. His Favorite color is {color}"
        # return super().student_details()

class SecondaryStudent(Student):
    pass

primary_details = PrimaryStudent(name="Pasan", age=28)
# for this the value should be passed as a assingment to the attribute
print(primary_details.student_details(color="red"))
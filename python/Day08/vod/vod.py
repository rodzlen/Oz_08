# class CreateOzStudents:
#     def __init__(self, name, python, database, django, AWS):
#         self.name = name
#         self.python = python
#         self.database = database
#         self.django = django
#         self.AWS = AWS

# def create_oz_students(name, python, database, django, AWS):
#     return {
#         "name": name,
#         "python": python,
#         "database": database,
#         "Django": django,
#         "AWS": AWS
#     }
    
# def get_sum(self):
#     return self.python + self.database + self.django + self.AWS
	
# def get_average(self):
#     return self.get_sum() / 4	
	
# def to_string(self):
#     return f'{self.name}\t{self.get_sum()}\t{self.get_average()}'

# oz_students = [
#     create_oz_students("백현우", 4, 3, 3, 2),
#     create_oz_students("홍혜인", 4, 5, 2, 4),
#     create_oz_students("윤은성", 3, 4, 4, 1),
#     create_oz_students("홍수철", 2, 3, 1, 5)
# ]

# print("이름", "총점", "평균", sep="\t")

# for student in oz_students:
#     ability_sum = student["python"] + student["database"] + student["Django"] + student["AWS"]
#     ability_average = ability_sum / 4
    
#     print(student["name"], ability_sum, ability_average, sep="\t")

# print("이름", "총점", "평균", sep="\t")

# for student in oz_students:
#     print( student.to_string())



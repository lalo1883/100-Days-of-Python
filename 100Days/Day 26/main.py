import random

names = ['Edy', 'Tina', 'David', 'Pepe', 'Nidia']

new_dict = {student:random.randint(1,100) for student in names}
print(new_dict)
passed_students = {student:score * 2 for (student, score) in new_dict.items() if score > 50}
print(passed_students)
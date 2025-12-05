

groupmates = [
    {
        "name": "Алексей",
        "surname": "Кутловский",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [4, 3, 5]
    },
    {
        "name": "Вениамин",
        "surname": "Старцев",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 4, 5]
    },
    {
        "name": "Анна",
        "surname": "Афанасьева",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 5, 5]
    }
]

def print_students(students):
    print("Имя".ljust(15), "Фамилия".ljust(10), "Экзамены".ljust(30), "Оценки".ljust(20))
    for student in students:
        print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(30), str(student["marks"]).ljust(20))

def filter_students(students, min_avg):
    result = []
    for student in students:
        avg = sum(student["marks"]) / len(student["marks"])
        if avg >= min_avg:
            result.append(student)
    return result

min_avg = float(input("Введите минимальный средний балл: "))
filtered = filter_students(groupmates, min_avg)
print_students(filtered)
try:
    lessons_dict = {}
    with open("C:\BSUIR\AcademicSubjects.txt", 'r', encoding="utf-8") as f1:
        lines = f1.readlines()
        for line in lines:
            parts = line.split(': ')

            subject = parts[0]
            lessonData = parts[1].strip()

            lessons = lessonData.split()

            totalLessons = 0

            for lesson in lessons:
                number_str = lesson.split('(')[0]
                if number_str.isdigit():
                    number = int(number_str)
                    totalLessons += number

            lessons_dict[subject] = totalLessons
except IOError:
    print("Произошла ошибка ввода-вывода")
finally:
    f1.close()

print(lessons_dict)

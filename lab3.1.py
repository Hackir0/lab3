import os
try:
    with open ( 'F1','w') as file1:
        while True:
            line = input()
            if line == "":
                break
            file1.write(line+"\n")
except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    file1.close()
try:
    with open('F1', 'r') as file1, open('F2', 'w') as file2:
        lines = file1.readlines()
        odd_lines = []
        for index, line in enumerate(lines):
            if index % 2 == 0:
                odd_lines.append(line)
        file2.writelines(odd_lines)
except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    file1.close()
    file2.close()
sizeFile1 = os.path.getsize("F1")
sizeFile2 = os.path.getsize("F2")
print(f"Размер файла F1: {sizeFile1} байт ")
print(f"Размер файла F2: {sizeFile2} байт ")
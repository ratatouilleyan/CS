students = ['Alissa', 'Ben', 'Charlie', 'Diana']
grades = ['B', 'D', 'B', 'A']

def find_grade(name, students, grades):
    found = False
    i = 0
    while not found and i < len(students):
        if students[i] == name:
            found = True
        i += 1
    if found:
        return(grades[i - 1])
    return None

print(find_grade('Charlie', students, grades))
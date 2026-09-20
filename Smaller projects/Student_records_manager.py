
student_records = {
    
}

def is_enrolled(name, course):
    if name in student_records:
        if course in student_records[name]['courses']:
            return True
        else:
            return False
    else:
        print(f"Student '{name}' not found.")
        return False

def add_student(name, age, courses):
    if name in student_records:
        print(f"Student '{name}' already exists.")
    
    student_records[name] = {'age': age, 'grades': set(), 'courses': courses}
    print(f"Student '{name}' added successfully.")

def add_grade(name, grade):
    if name in student_records:
        student_records[name]['grades'].add(grade)
        print(f"Grade {grade} added for student '{name}'.")
    else:    
        print(f"Student '{name}' not found.")

def calculate_average_grade(name):
    if name in student_records:
        if student_records[name]['grades']:
            average = sum(student_records[name]['grades'])/len(student_records[name]['grades'])
            return average
        else:
            return 0
    else:
        print(f"Student {name} not found.")
        return None

def list_students_by_course(course):
    students_in_course = [name for name, info in student_records.items() if course in info['courses']]
    if students_in_course:
        return students_in_course
    else:
        return []
    
def filter_top_students(threshold):
    smart_kids = [name for name in student_records if calculate_average_grade(name) > threshold]
    return smart_kids

add_student("Alice", 20, ["Math", "Physics"])
add_student("Bob", 22, ["Biology", "Chemistry"])
add_grade("Alice", 90)
add_grade("Alice", 85)
add_grade("Bob", 75)
add_grade("Charlie", 80)  # Non-existent student
print(is_enrolled("Alice", "Math"))  # Should return True
print(is_enrolled("Alice", "Biology"))  # Should return False
print(is_enrolled("Bob", "Biology"))  # Should return True
print(is_enrolled("Charlie", "Math"))  # Non-existent student, should print message and return F.
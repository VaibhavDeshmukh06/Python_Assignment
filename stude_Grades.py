student_grades = {"Vaibhav": "A", "Kartik": "B"}  

# Add a new student and grade
name = "Raj"
grade = "C"
if name not in student_grades:
    student_grades[name] = grade
else:
    print(f"{name} already exists.")

# Update an existing student's grade
name = "Vaibhav"
new_grade = "D"
if name in student_grades:
    student_grades[name] = new_grade
else:
    print(f"{name} does not exist.")

# Print all student grades
for name, grade in student_grades.items():
    print(f"{name}: {grade}")

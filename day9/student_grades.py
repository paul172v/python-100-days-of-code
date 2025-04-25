student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for student in student_scores:
    if student_scores[student] > 90:
        student_grades[student] = 'Outstanding'
    if student_scores[student] > 80 and student_scores[student] <= 90:
        student_grades[student] = 'Exceeds Expectations'
    if student_scores[student] > 70 and student_scores[student] <= 80:
        student_grades[student] = 'Acceptable'
    if student_scores[student] <= 70: 
        student_grades[student] = 'Fair'
    
print(student_grades)


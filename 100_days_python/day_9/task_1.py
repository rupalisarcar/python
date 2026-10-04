student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for student in student_scores:
    grades=''   
    if student_scores[student]>=91 and student_scores[student]<100:
        grades = "Outstanding" 

    elif student_scores[student]>=81 and student_scores[student]<90:
        grades = "Exceeds Expectations"
    
    elif student_scores[student]>=71 and student_scores[student]<80:
        grades = "Acceptable" 
    
    else:
        grades = "Fail" 

    student_grades[student] = grades

    

print(student_grades)

    
students_score = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64,89]

#1st option
score = sum(students_score)
print(score)

#2nd Option
sum = 0
for score in students_score:
    sum+=score
print(f"Total score is : {sum}")

#1st option for Maximum Number
highest_number = max(students_score)
print(highest_number)

#2nd option for Maximum Number
maximum_number = 0

for score in students_score:
    if score>maximum_number:
        maximum_number = score

print(f"Maximum number is {maximum_number}")

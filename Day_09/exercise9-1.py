student_scores = {
    "Dirty Harry": 81,
    "Ron The Drinker": 78,
    "Hediondo": 99,
    "Wasted": 74,
    "Poohead": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.
student_grades={}

# TODO-2: Write your code below to add the grades to student_grades.👇
for student in student_scores:
    score=student_scores[student]
    if score >= 91 and score <= 100:
        student_grades[student]='Outstanding'
    elif score>=81:
        student_grades[student] = 'Exceeds Expectation'
    elif score>=71:
        student_grades[student] = 'Acceptable'
    elif score <=70:
        student_grades[student] = 'FAIL'


# 🚨 Don't change the code below 👇
print(student_grades)
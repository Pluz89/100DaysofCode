
# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split(', ')
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
max=0
min=100
for score in student_scores:
  if score>max:
    max=score
  if score<min:
    min=score


print('max value is: ', max)
print('min value is: ', min)
import random

#Asssumption that the student has taken 10 courses
num_courses = 10
total_sum = 0

# Ask the user to enter final scores for each course
for course_number in range(1, num_courses + 1):
    score = int(input(f"Enter the final score for course {course_number}: "))
    total_sum += score

# Calculate average
average = total_sum / num_courses

# Determine the grade based on the scale
if average > 90:
    grade = "A"
elif average > 80:
    grade = "B"
elif 75 <= average <= 79:
    grade = "C"
elif average > 60:
    grade = "D"
else:
    grade = "F"

# Print the results
print("\nTotal Sum:" , total_sum)
print("Average:" ,average)
print("Grade:" , grade)



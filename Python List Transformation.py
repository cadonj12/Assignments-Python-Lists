#Task 1

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort(reverse=True)
print(grades)


#Task 2

average_grade = sum(grades) / len(grades)
print(average_grade)


#Task 3

for i in range(len(grades)):
    if grades[i] < 80:
        grades[i] = "Failed"
print(grades)
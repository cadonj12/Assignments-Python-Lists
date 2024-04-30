#Task 1

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

good_students = [student for student in submitted if student in attended]
print(good_students)


#Task 2

submitted.sort()
attended.sort()

are_identical = submitted == attended
print(are_identical)


#Task 3

attended.remove("Eve")
attended.remove("Frank")
print(attended)
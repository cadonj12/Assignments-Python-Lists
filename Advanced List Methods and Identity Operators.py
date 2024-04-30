#Task 1

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

good_students = [student for student in submitted if student in attended]
print(good_students)

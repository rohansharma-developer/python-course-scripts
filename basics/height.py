student_heights = [180, 124, 165, 173, 189, 169, 146]

students = 0
total_height = 0
for height in student_heights:
    students += 1
    total_height += height
print(f"The total height is: {total_height}")
print(f"The total number of students are: {students}")
avg = int(total_height / students)
print(f"The average height of students is: {avg}")

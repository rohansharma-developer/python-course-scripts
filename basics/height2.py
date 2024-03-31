student_heights = [180, 124, 165, 273, 189, 169, 146]
highest_score = 0
for height in student_heights:
    if highest_score < height:
        highest_score = height

print(f"The highest score is {highest_score}")
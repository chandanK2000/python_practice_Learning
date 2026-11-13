
import marks

student_name = "Chandan"

maths = 80
science = 90
english = 70

total = marks.calculate_total(maths, science, english)

percentage = marks.calculate_percentage(total)

print("Student Name:", student_name)
print("Total Marks:", total)
print("Percentage:", percentage)

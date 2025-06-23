num_students = int(input("Enter number of students: "))

# This will hold dictionaries like {'name': 'Alice', 'average': 85, 'grade': 'A'}
students =[]

# Use aa loop to get info for each student
# We loop num_students name and marks: 
for i in range(num_students):
    print(f"\nEnter details for the students {i + 1}:")
    name = input("Enter name: ")

    #ask for 3 marks 
    mark1 = float(input("Enter mark1: "))
    mark2 = float(input("Enter mark2: "))
    mark3 = float(input("Enter mark3: "))
    # calculate average 
    average = (mark1 + mark2 + mark3) / 3

    # Determine Grade using if-else
if average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >=60:
    grade = "C"
elif average >=50:
    grade = "D"
else:
    grade ="F" 

# Store the Data, Now we save the info in the list:
students_data = {
    'name': name,
    'average': average,
    'grade': grade
}
students.append(students_data)

# print the report, after the loop ends, we print all students' results:
print ("\n== Grade Report ===")
for student in students:
    print(f"Name: {student['name']} | Average: {student['average']:.2f} |Grade: {student['grade']}") 
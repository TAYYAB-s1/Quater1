students = []
while True:
    name = input("Please enter the student's name (or type 'stop' to finish): ")
    if name == "stop":
        break
    if name in students:
        print("This name is already in the list.")
        continue
    students.append(name)

students_with_ids = [(i+1, name) for i, name in enumerate(students)]

print("Complete List of Students (Tuples):\n", students_with_ids)


print("List of Students with IDs:")
for id, name in students_with_ids:
    print(f"ID: {id}, Name: {name}")

total_students = len(students)
total_name_length = sum(len(name) for name in students)

longest_name_student = max(students, key=len)
shortest_name_student = min(students, key=len)

print("\nTotal number of students:", total_students)
print("Total length of all student names combined:", total_name_length)
print("The student with the longest name is:", longest_name_student)
print("The student with the shortest name is:", shortest_name_student)

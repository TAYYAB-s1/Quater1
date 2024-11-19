class Student:
    def __init__(self, name, math, science, english):
        self.name = name
        self.scores = {"math": math, "science": science, "english": english} 

    def calculate_average(self):
        total = sum(self.scores.values())
        return total / len(self.scores)

    def is_passing(self, passing_threshold=60):
        return self.calculate_average() >= passing_threshold

    def get_highest_score(self):
        return max(self.scores.values())
 
    def get_lowest_score(self):
        return min(self.scores.values())

def main():
    students = []
    num_students = int(input("Enter the number of students: "))

    for i in range(num_students):
        name = input("Enter student name: ")
        math = float(input("Enter math score: "))
        science = float(input("Enter science score: "))
        english = float(input("Enter english score: "))
        student = Student(name, math, science, english)
        students.append(student)

    for student in students:
        print(f"Student: {student.name}")
        print(f"Average Score: {student.calculate_average()}")
        print(f"Passing: {student.is_passing()}")
        print(f"Highest Score: {student.get_highest_score()}")
        print(f"Lowest Score: {student.get_lowest_score()}")
        print()

    # Calculate class statistics
    class_average = sum(student.calculate_average() for student in students) / num_students
    num_passing = sum(1 for student in students if student.is_passing())
    num_failing = num_students - num_passing

    print("Class Statistics:")
    print(f"Class Average: {class_average}")
    print(f"Number of Students Passing: {num_passing}")
    print(f"Number of Students Failing: {num_failing}")

if __name__ == "__main__":
    main()
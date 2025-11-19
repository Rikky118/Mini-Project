# List of students
students = ["Alice", "Bob", "Charlie", "David", "Eva"]

# Dictionary to store attendance records for each student
attendance = {}

# Input attendance for each student
for student in students:
    total_classes = int(input(f"Enter total classes for {student}: "))
    present_classes = int(input(f"Enter present classes for {student}: "))
    percentage = (present_classes / total_classes) * 100
    attendance[student] = {
        "total": total_classes,
        "present": present_classes,
        "percentage": round(percentage, 2)
    }

# Display attendance percentage for each student
print("\nAttendance Report:")
print("-" * 40)
for student, data in attendance.items():
    print(f"{student}: {data['percentage']}%")
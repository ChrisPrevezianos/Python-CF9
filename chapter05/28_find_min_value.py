def main():
    student_grades = {
        "Alice": 85,
        "Bob": 72,
        "Charlie": 88,
        "Diana": 90,
        "Eve": 67
    }

    student_with_lowest_grade = min(student_grades, key=student_grades.get)
    print(f"Student with the lowest grade: {student_with_lowest_grade} has grade: {student_grades[student_with_lowest_grade]}")

    # Find the student with the smallest name (alphabetically)
    student_with_smallest_name_alpha = min(student_grades)
    print(student_with_smallest_name_alpha)

    # Fnd thhe student with the shortest name by length
    student_with_shortest_name = min(student_grades, key=len)
    print(student_with_shortest_name)

if __name__ == "__main__":
    main()
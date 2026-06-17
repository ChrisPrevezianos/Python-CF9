students = {
    "Alice": [],
    "Bob": [79, 95, 88],
    "Charlie": [68, 72, 80],
    "Diana": [95, 98, 100],
    "Eve": [50, 60, 58]
}
 
def main():
    while True:
        try:
            threshold = int(input("Please insert the threshold (int): "))
            break
        except ValueError:
            print("Invalid input. Please give me an integer.")
 
    average_grades = {
        student : round(sum(grades) / len(grades), 2)
        for student, grades in students.items()
        if grades and round(sum(grades) / len(grades), 2) > threshold
    }
   
    for student, avg_grades in average_grades.items():
        print(f"{student} : {avg_grades:.2f}")
   
if __name__ == "__main__":
    main()

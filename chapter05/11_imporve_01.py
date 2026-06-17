def upscale_grades(grades):
    upscaled = [grade + 1 if grade <=9 else grade for grade in grades]
    return upscaled
 
def filter_passed(grades):
    passed = [grade for grade in grades if grade >= 5]
    return passed
 
def categorize_grades(grades):
    passed = [grade for grade in grades if grade >= 5]
    failed = [grade for grade in grades if grade < 5]
    honors = [grade for grade in grades if grade == 10]
    return passed, failed, honors
 
def calculate_average(grades):
    return sum(grades) / len(grades) if grades else 0
 
def main():
    grades = [7, 5, 9, 10, 3, 6, 8, 4, 10, 2]
 
    upscaled_grades = upscale_grades(grades)
    print(f"Original grades: {grades}")
    print(f"Upscaled grades: {upscaled_grades}")
 
    passed_grades = filter_passed(grades)
    print(f"Passed grades: {passed_grades}")
 
    passed, failed, honors = categorize_grades(grades)
    print(f"passed: {passed}")
    print(f"failed: {failed}")
    print(f"honors: {honors}")
 
    average_grade = calculate_average(grades)
    print(f"Average grade: {average_grade}")
 
if __name__ == "__main__":
    main()
def main():
    grades = [7, 5, 9, 10, 3]
 
    # upscale grades by 1 using list compr !
    upscaled_grades = [grade + 1 if grade <= 9 else grade for grade in grades]
    print(f"Upscladed grades: {upscaled_grades}")
 
    # Map (Transforms the data of the list) using map() function
    upscaled_grades_2 = list(map(lambda grade: grade + 1 if grade <=9 else grade, grades))
 
 
    # Filter using list comp
    passed_grades = [grade for grade in grades if grade >= 5]
 
 
    # Filter (base on a predicate) using filter function
    passed_grades_2 = list(filter(lambda grade: grade >= 5, grades))
 
if __name__ == "__main__":
    main()
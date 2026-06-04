name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
height = float(input("Please enter your height: "))
is_student = input("Are you a student? (yes/no):").lower() == "yes"

if is_student:
    print("You are student")
else:
    print("Yoy are teacher")

# if is_student == "yes":
#     print("You are student")
# else:
#     print("You are teacher")

# print("Your age is {}, and your height is {:.2f} meters.".format(age, height))
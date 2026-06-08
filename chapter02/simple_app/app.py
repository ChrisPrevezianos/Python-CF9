# import my_calc
from my_calc import my_add_function as my_add, num1

num2 = 10

# res = my_calc.my_add_function(num2, 100)
res = my_add(num2, num1)
print(res)
print(f"This comes from app.py: {__name__}")
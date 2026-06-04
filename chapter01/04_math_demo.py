import math

name = "Alice"
age = 20

print("CF9")

print("PI =", math.pi)

print(name + " is " + str(age) + " years old.")

print("Python 2 style")
print("PI = %6.2f" % math.pi)
print("%s is %d years old" %(name, age))

print("Python 3 style using string format")
print("Age is {0:2d}".format(age))
print("PI is {0:.3f}".format(math.pi))

print("{0} is {1} years old".format(name, age))

print("{0:*^10}:{1:>20}".format(name, age))
print("{0:*^10}:{1:<20}".format(name, age), end='.')

print("Python 3 style using f-strings") # we love f-string
print(f"{name} is {age} years old.")
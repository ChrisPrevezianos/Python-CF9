# range(start, end, step)
# start: inclusive
# end: exclusive

# print odd numbers from 1 to 21
print("Java Style")
for i in range(22):
    if i % 2 != 0:
        print(i, end=' ')
print()

print("Python style")
for i in range(1, 22, 2):
    print(i, end=' ')
print()
students = {
    10: "Alice",
    20: "Bob",
    5: "Charlie",
    "numbers": [1, 3, 5]
}

for key, value in students.items():
    print(f"{key} : {value}")

# ---------------------------------

strange_dict = {
    "key1" : "value1",
    "key2" : 10,
    3: "three",
    4: [1, 2, 3, 4],
    True: 100,
    (1,2,3): "my tuple",
    frozenset({1, 5, 10}): "my set"
    # {1, 5, 10}: "my set"
    # [10, 20, 30]: "my list"
}

print(strange_dict)
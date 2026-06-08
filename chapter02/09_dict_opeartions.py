# Dictionary CRUD functions

# Initialize a dictionary of products
products = {
    1: "apples",
    2: "bananas",
    3: "melons"
}

print(products[1]) # get a value based on Key

# products[1] = "cherries"
# print(products)

# update / insert
products[10] = "cherries"
print(products)

# product_10 = products.get(10)
# print(product_10)

product_10 = products.get(100, "not found") # get a value based on key
print(product_10)

del products[1]
print(f"After deleting key-value pair with key:1 : {products}")

# Delete: ...
value = products.pop(2)
print(value)
print(products)

key, value = products.popitem() # (10, 'cherries)
print(key, value)

new_products = {
    1: "apples",
    2: "bananas",
    3: "melons"
}

# i want to check if a key exists in my dict
key_to_check = "apples"

if key_to_check in new_products:
    print(f"{key_to_check} key exists and its value is: {new_products[key_to_check]}")
else:
    print(f"{key_to_check} does not exist!")

for key in new_products:
    print(key)
print()

for key in new_products.keys():
    print(f"{key}:{new_products[key]}")
print()

for value in new_products.values():
    print(value)

# iterate a dict with key and value
for key, value in new_products.items():
    print(f"{key}:{value}")
# set -> {}

bag = {"eggs", "apples", "milk", "bananas", "eggs"}
print(f"Initial bag: {bag}")

bag.add("oranges")
bag.add("oranges")
bag.add("oranges")
print(f"Bag after adding oranges: {bag}")

# bag.append("Nikias")
print()
# iterate with enhanced for
for item in bag:
    print(item, end=", ")
print()

# remove from sets
item_to_remove = "eggs"
bag.remove(item_to_remove) 
print(f"Bag after removing {item_to_remove}: {bag}")

if item_to_remove in bag:
    bag.remove(item_to_remove)
    print(f"{item_to_remove} removed.")
else: 
    print (f"{item_to_remove} not in set!")
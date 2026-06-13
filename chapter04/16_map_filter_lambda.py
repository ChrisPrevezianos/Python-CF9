cities = ["london", "paris", "barcelona", "athens", "Casablanka"]

# Filtering city names longer than 5 character using filter and lambda
long_cities = filter(lambda city: len(city) > 5, cities)

# Capitalize the filter cities using mapp and lambda
cap_length_cities = map(lambda city: city.title(), long_cities)

# All in one
cap_long_cities = list(map(lambda city: city.title(), filter(lambda city: len(city) > 5, cities)))
print(*cap_long_cities)

# Usining list comprehension
cap_length_cities_comp = [city.title() for city in cities if len(city) > 5]
print(cap_length_cities_comp)
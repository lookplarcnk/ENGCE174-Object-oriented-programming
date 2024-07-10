names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
city = ["New York", "Los Angeles", "Chicago"]

# Using zip() for parallel iteration
for name, age, city in zip(names, ages, city):
    print(f"{name} is {age} years old and lives in {city}")
# Output:
# Alice is 25 years old and lives in New York
# Bob is 30 years old and lives in Los Angeles
# Charlie is 35 years old and lives in Chicago
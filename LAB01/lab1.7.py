# Tuple initialization
coordinates = (3, 5)

# Unpacking tuples
x, y = coordinates
print("x-coordinate:", x)   # Output: 3
print("y-coordinate:", y)   # Output: 5

# Tuple as keys in dictionary
location = {(3, 5): "Home", (10, 20): "Office"}
print("Location at (3, 5):", location[(3, 5)])  # Output: Home
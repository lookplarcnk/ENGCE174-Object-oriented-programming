# Example 2: List comprehension to create a new list แสดงการใช้ list comprehension เพื่อสร้างลิสต์ใหม่

# Creating a list of squares of numbers from 1 to 5 สร้างลิสต์ของเลขยกกำลังสองจาก 1 ถึง 5
squares = [x ** 2 for x in range(1, 6)]

print("Squares:", squares) # Output: [1, 4, 9, 16, 25]
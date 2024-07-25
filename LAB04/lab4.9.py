# Example 1: Working with dictionaries การทำงานกับดิกชันนารี

# Creating a dictionary of student grades สร้างดิกชันนารีของเกรดนักเรียน
grades = {'Alice': 85, 'Bob': 92, 'Charlie': 88, 'David': 95}

# Accessing values using keys เข้าถึงค่าโดยใช้คีย์
print("Bob's grade:", grades['Bob']) # Output: Bob's grade: 92 แสดงผล: Bob's grade: 92

# Adding a new entry เพิ่มข้อมูลใหม่
grades['Eve'] = 90

# Iterating through keys and values การวนลูปผ่านคีย์และค่า
for student, grade in grades.items():
    print(f"{student}: {grade}")
    
# Using get() method to avoid KeyError ใช้เมธอด get() เพื่อลดโอกาสการเกิด KeyError
print("Frank's garde:", grades.get('Frank','Grade not found')) # Output: Frank's grade: Grade not found แสดงผล: Frank's grade: Grade not found
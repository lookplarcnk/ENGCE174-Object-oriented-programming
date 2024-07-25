# Example 4: Set operations and methods การดำเนินการและเมธอดของชุดข้อมูล (Sets)

# ชุดข้อมูล (Sets)
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Adding elements to a set การเพิ่มองค์ประกอบลงในชุดข้อมูล
set1.add(5)

# Removing elements from a set การลบองค์ประกอบออกจากชุดข้อมูล
set2.discard(6)

# Checking subset and superset การตรวจสอบ subset และ superset
print("Is set1 a subset of set2?", set1.issubset(set2)) # Output: Is set1 a subset of set2? False แสดงผล: Is set1 a subset of set2? False
print("Is set2 a superset of set1?", set2.issuperset(set1)) # Output: Is set2 a superset of set1? True แสดงผล: Is set2 a superset of set1? True
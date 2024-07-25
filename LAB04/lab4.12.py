# Example 5: Using sets for unique operations การใช้ชุดข้อมูล (Sets) สำหรับการดำเนินการกับข้อมูลที่ไม่ซ้ำ

# Finding unique elements from multiple lists การหาสมาชิกที่ไม่ซ้ำจากหลายลิสต์
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
list3 = [5, 6, 7, 8, 9]

# แปลงลิสต์เป็นชุดข้อมูลแล้วใช้การรวมและความแตกต่าง
unique_elements = set(list1).union(set(list2)).difference(set(list3))
print("Unique elements:", unique_elements) # Output: Unique elements: {1, 2} แสดงผล: Unique elements: {1, 2}
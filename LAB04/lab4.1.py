# Example 1: Creating and manipulating lists แสดงวิธีการสร้างและจัดการกับลิสต์

# Creating a list of numbers สร้างลิสต์ของตัวเลข
numbers = [1, 2, 3, 4, 5]

# Adding elements to the end of the list เพิ่มองค์ประกอบที่ส่วนท้ายของลิสต์
numbers.append(6)

# Modifying an element at a specific index แก้ไของค์ประกอบที่ตำแหน่งเฉพาะ
numbers[2] = 10

# Removing an element by value ลบองค์ประกอบตามค่า
numbers.remove(4)

print("Updated list:", numbers) # Output: [1, 2, 10, 5, 6] แสดงผล: [1, 2, 10, 5, 6]
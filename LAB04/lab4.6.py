# Given a list of numbers, remove all occurrences of a specific number and calculate the sum of remaining numbers.

# ลิสต์ของตัวเลข
numbers = [1, 2, 3, 4, 5, 3, 6, 7, 3]
remove_num = 3

# ลบทุกการปรากฏของหมายเลขที่ต้องการ
while remove_num in numbers:
    numbers.remove(remove_num)

# แสดงผลลัพธ์ของลิสต์หลังจากการลบ
print("Numbers after removal:", numbers) # แสดงผล: Numbers after removal: [1, 2, 4, 5, 6, 7]

# คำนวณผลรวมของตัวเลขที่เหลือ
print("Sum of remaining numbers:", sum(numbers)) # แสดงผล: Sum of remaining numbers: 25
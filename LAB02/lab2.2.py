# 1. Left half pyramid ปิรามิดครึ่งซ้าย
num_rows = int(input("Enter the number of rows : "))  # รับค่าจำนวนแถวจากผู้ใช้
# สร้างรูปแบบปิรามิดครึ่งซ้ายโดยไม่ใช้ loop ทั้งหมด
pyramid_rows = map(lambda i: ' '.join(['*'] * (i + 1)), range(num_rows))
# พิมพ์ผลลัพธ์
print('\n'.join(pyramid_rows))
    
# 2. Inverted half pyramid ปิรามิดหัวกลับ
num_rows = int(input("Enter the number of rows : "))  # รับค่าจำนวนแถวจากผู้ใช้
# สร้างหรือสร้างรูปแบบสามเหลี่ยมโดยไม่ใช้ loop ทั้งหมด
pyramid_rows = map(lambda i: ' '.join(['*'] * (num_rows - i)), range(num_rows))
# พิมพ์ผลลัพธ์
print('\n'.join(pyramid_rows))
    
# 3. Full pyramid ปิรามิดเต็ม
num_rows = int(input("Enter the number of rows : "))  # รับค่าจำนวนแถวจากผู้ใช้
# สร้างรูปแบบปิรามิดเต็มโดยไม่ใช้ loop ทั้งหมด
pyramid_rows = map(lambda i: ' ' * (num_rows - i - 1) + '* ' * (i + 1), range(num_rows))
# พิมพ์ผลลัพธ์
print('\n'.join(pyramid_rows))

# 4. Inverted full pyramid ปิรามิดเต็มหัวกลับ
num_rows = int(input("Enter the number of rows : "))  # รับค่าจำนวนแถวจากผู้ใช้
# สร้างรูปแบบปิรามิดเต็มหัวกลับโดยไม่ใช้ loop ทั้งหมด
pyramid_rows = map(lambda i: ' ' * i + '* ' * (num_rows - i), range(num_rows))
# พิมพ์ผลลัพธ์
print('\n'.join(pyramid_rows))
    
# 5. Right half pyramid ปิรามิดครึ่งซ้าย
num_rows = int(input("Enter the number of rows : "))  # รับค่าจำนวนแถวจากผู้ใช้
# สร้าง Right half pyramid โดยไม่ใช้ loop ทั้งหมด
pyramid_rows = map(lambda i:' ' * (num_rows - i - 1) + '*' * (i + 1), range(num_rows))
# พิมพ์ผลลัพธ์
print('\n'.join(pyramid_rows))


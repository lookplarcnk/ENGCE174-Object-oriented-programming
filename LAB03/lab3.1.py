# 1. Left half pyramid ปิรามิดครึ่งซ้าย
def left_half_pyramid(num_rows):
    pyramid_rows = []  # สร้างลิสต์เปล่าสำหรับเก็บแถวของปิรามิด
    for i in range(1, num_rows + 1):  # ลูปวนจาก 1 ถึงจำนวนแถวที่ผู้ใช้ป้อน
        row = " ".join(["*"] * i)  # สร้างแถวโดยใช้ * คูณด้วย i และแยกด้วยช่องว่าง
        pyramid_rows.append(row)  # เพิ่มแถวที่สร้างเข้าไปในลิสต์
    return pyramid_rows  # คืนค่าลิสต์ที่มีแถวของปิรามิด

# 2. Inverted half pyramid ปิรามิดหัวกลับ
def inverted_half_pyramid(num_rows):
    pyramid_rows = []  # สร้างลิสต์เปล่าสำหรับเก็บแถวของปิรามิดหัวกลับ
    for i in range(num_rows):  # ลูปวนจาก 0 ถึงจำนวนแถวที่ผู้ใช้ป้อน
        row = " ".join(["*"] * (num_rows - i))  # สร้างแถวโดยใช้ * คูณด้วยจำนวนแถวที่เหลืออยู่
        pyramid_rows.append(row)  # เพิ่มแถวที่สร้างเข้าไปในลิสต์
    return pyramid_rows  # คืนค่าลิสต์ที่มีแถวของปิรามิดหัวกลับ

# 3. Full pyramid ปิรามิดเต็ม
def full_pyramid(num_rows):
    pyramid_rows = []  # สร้างลิสต์เปล่าสำหรับเก็บแถวของปิรามิดเต็ม
    for i in range(num_rows):  # ลูปวนจาก 0 ถึงจำนวนแถวที่ผู้ใช้ป้อน
        row = " " * (num_rows - i - 1) + "* " * (i + 1)  # สร้างแถวโดยมีช่องว่างข้างหน้าตามจำนวนแถวที่เหลืออยู่และ * ตามจำนวนแถวปัจจุบัน
        pyramid_rows.append(row)  # เพิ่มแถวที่สร้างเข้าไปในลิสต์
    return pyramid_rows  # คืนค่าลิสต์ที่มีแถวของปิรามิดเต็ม

# 4. Inverted full pyramid ปิรามิดเต็มหัวกลับ
def inverted_full_pyramid(num_rows):
    pyramid_rows = []  # สร้างลิสต์เปล่าสำหรับเก็บแถวของปิรามิดเต็มหัวกลับ
    for i in range(num_rows, 0, -1):  # ลูปวนจากจำนวนแถวที่ผู้ใช้ป้อนจนถึง 1
        row = " " * (num_rows - i) + "* " * i  # สร้างแถวโดยมีช่องว่างข้างหน้าตามจำนวนแถวที่เหลืออยู่และ * ตามจำนวนแถวปัจจุบัน
        pyramid_rows.append(row)  # เพิ่มแถวที่สร้างเข้าไปในลิสต์
    return pyramid_rows  # คืนค่าลิสต์ที่มีแถวของปิรามิดเต็มหัวกลับ

# 5. Right half pyramid ปิรามิดครึ่งขวา
def right_half_pyramid(num_rows):
    pyramid_rows = []  # สร้างลิสต์เปล่าสำหรับเก็บแถวของปิรามิดครึ่งขวา
    for i in range(num_rows):  # ลูปวนจาก 0 ถึงจำนวนแถวที่ผู้ใช้ป้อน
        row = " " * (num_rows - i - 1) + "*" * (i + 1)  # สร้างแถวโดยมีช่องว่างข้างหน้าตามจำนวนแถวที่เหลืออยู่และ * ตามจำนวนแถวปัจจุบัน
        pyramid_rows.append(row)  # เพิ่มแถวที่สร้างเข้าไปในลิสต์
    return pyramid_rows  # คืนค่าลิสต์ที่มีแถวของปิรามิดครึ่งขวา

# ฟังก์ชันเพื่อคืนค่าแถวของปิรามิดหลายๆ แบบ
def generate_pyramids(num_rows):
    left = left_half_pyramid(num_rows)  # เรียกใช้ฟังก์ชันสร้างปิรามิดครึ่งซ้าย
    inverted_left = inverted_half_pyramid(num_rows)  # เรียกใช้ฟังก์ชันสร้างปิรามิดหัวกลับ
    full = full_pyramid(num_rows)  # เรียกใช้ฟังก์ชันสร้างปิรามิดเต็ม
    inverted_full = inverted_full_pyramid(num_rows)  # เรียกใช้ฟังก์ชันสร้างปิรามิดเต็มหัวกลับ
    right = right_half_pyramid(num_rows)  # เรียกใช้ฟังก์ชันสร้างปิรามิดครึ่งขวา
    return left, inverted_left, full, inverted_full, right  # คืนค่าแถวของปิรามิดทั้งหมด

# ทดสอบฟังก์ชัน
num_rows = int(input("Enter the number of rows : "))  # รับค่าจำนวนแถวจากผู้ใช้
left, inverted_left, full, inverted_full, right = generate_pyramids(num_rows)  # เรียกใช้ฟังก์ชันเพื่อสร้างปิรามิด

print("Left half pyramid :")
print("\n".join(left))  # แสดงผลลัพธ์ของปิรามิดครึ่งซ้าย

print("\nInverted half pyramid :")
print("\n".join(inverted_left))  # แสดงผลลัพธ์ของปิรามิดหัวกลับ

print("\nFull pyramid :")
print("\n".join(full))  # แสดงผลลัพธ์ของปิรามิดเต็ม

print("\nInverted full pyramid :")
print("\n".join(inverted_full))  # แสดงผลลัพธ์ของปิรามิดเต็มหัวกลับ

print("\nRight half pyramid :")
print("\n".join(right))  # แสดงผลลัพธ์ของปิรามิดครึ่งขวา
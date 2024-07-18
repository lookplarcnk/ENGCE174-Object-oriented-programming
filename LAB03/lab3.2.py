# 1. Left half pyramid ปิรามิดครึ่งซ้าย
def left_half_pyramid(num_rows):
    pyramid_rows = map(lambda i: ' '.join(['*'] * (i + 1)), range(num_rows))
    return tuple(pyramid_rows)

# 2. Inverted half pyramid ปิรามิดหัวกลับ
def inverted_half_pyramid(num_rows):
    pyramid_rows = map(lambda i: ' '.join(['*'] * (num_rows - i)), range(num_rows))
    return tuple(pyramid_rows)

# 3. Full pyramid ปิรามิดเต็ม
def full_pyramid(num_rows):
    pyramid_rows = map(lambda i: ' ' * (num_rows - i - 1) + '* ' * (i + 1), range(num_rows))
    return tuple(pyramid_rows)

# 4. Inverted full pyramid ปิรามิดเต็มหัวกลับ
def inverted_full_pyramid(num_rows):
    pyramid_rows = map(lambda i: ' ' * i + '* ' * (num_rows - i), range(num_rows))
    return tuple(pyramid_rows)

# 5. Right half pyramid ปิรามิดครึ่งขวา
def right_half_pyramid(num_rows):
    pyramid_rows = map(lambda i: ' ' * (num_rows - i - 1) + '*' * (i + 1), range(num_rows))
    return tuple(pyramid_rows)

# ฟังก์ชันเพื่อคืนค่าแถวของปิรามิดหลายๆ แบบ
def generate_pyramids(num_rows):
    left = left_half_pyramid(num_rows)
    inverted_left = inverted_half_pyramid(num_rows)
    full = full_pyramid(num_rows)
    inverted_full = inverted_full_pyramid(num_rows)
    right = right_half_pyramid(num_rows)
    return left, inverted_left, full, inverted_full, right

# ทดสอบฟังก์ชัน
num_rows = int(input("Enter the number of rows : "))  # รับค่าจำนวนแถวจากผู้ใช้
left, inverted_left, full, inverted_full, right = generate_pyramids(num_rows)

print("Left half pyramid :")
print('\n'.join(left))  # แสดงผลลัพธ์ของปิรามิดครึ่งซ้าย

print("\nInverted half pyramid :")
print('\n'.join(inverted_left))  # แสดงผลลัพธ์ของปิรามิดหัวกลับ

print("\nFull pyramid :")
print('\n'.join(full))  # แสดงผลลัพธ์ของปิรามิดเต็ม

print("\nInverted full pyramid :")
print('\n'.join(inverted_full))  # แสดงผลลัพธ์ของปิรามิดเต็มหัวกลับ

print("\nRight half pyramid :")
print('\n'.join(right))  # แสดงผลลัพธ์ของปิรามิดครึ่งขวา
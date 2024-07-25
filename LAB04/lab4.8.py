# สร้างชุดข้อมูลของตัวเลขคู่จาก 1 ถึง 10
even_numbers = {x for x in range(1, 11) if x % 2 == 0}

print("Even numbers:", even_numbers) # แสดงผล: Even numbers: {2, 4, 6, 8, 10}
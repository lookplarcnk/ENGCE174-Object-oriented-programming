# การสร้างรายการ (List comprehension)
squares = [x**2 for x in range(10)]
print(squares)  # แสดงผลลัพธ์ของรายการ

# การสร้างพจนานุกรม (Dictionary comprehension)
square_dict = {x: x**2 for x in range(5)}
print(square_dict)  # แสดงผลลัพธ์ของพจนานุกรม

# การสร้างเซ็ต (Set comprehension)
even_squares = {x**2 for x in range(10) if x % 2 == 0}
print(even_squares)  # แสดงผลลัพธ์ของเซ็ต
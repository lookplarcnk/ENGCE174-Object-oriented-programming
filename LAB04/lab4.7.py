# ชุดข้อมูล (Sets)
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# การรวมชุดข้อมูล (Union)
union_set = set1 | set2
print("Union:", union_set) # แสดงผล: Union: {1, 2, 3, 4, 5, 6}

# การตัดกันของชุดข้อมูล (Intersection)
intersection_set = set1 & set2
print("Intersection:", intersection_set) # แสดงผล: Intersection: {3, 4}

# ความแตกต่างระหว่างชุดข้อมูล (Difference)
difference_set = set1 - set2
print("Difference:", difference_set) # แสดงผล: Difference: {1, 2}

# ความแตกต่างแบบสมมาตร (Symmetric Difference)
symmetric_difference_set = set1 ^ set2
print("Symmetric Difference:", symmetric_difference_set) # แสดงผล: Symmetric Difference: {1, 2, 5, 6}
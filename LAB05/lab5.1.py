class Employee:
    def __init__(self, name, salary): # กำหนดชื่อและเงินเดือนของพนักงาน
        self.name = name # ใช้ self เพื่อกำหนดคุณสมบัติ name ของออบเจ็กต์
        self.salary = salary # ใช้ self เพื่อกำหนดคุณสมบัติ salary ของออบเจ็กต์

    def annual_salary(self): # ฟังก์ชันคำนวณเงินเดือนรายปี
        return self.salary * 12 # คืนค่าจำนวนเงินเดือนรายปี (เงินเดือน * 12 เดือน)

class Manager(Employee): # คลาส Manager สืบทอดคุณสมบัติและพฤติกรรมจากคลาส Employee
    def __init__(self, name, salary, bonus): # กำหนดชื่อ, เงินเดือน, และโบนัสสำหรับผู้จัดการ
        super().__init__(name, salary) # เรียกใช้งานฟังก์ชัน __init__ ของคลาส Employee
        self.bonus = bonus # กำหนดค่าโบนัสที่รับมาให้กับคุณสมบัติ bonus ของออบเจ็กต์

    def annual_salary(self): # ฟังก์ชันคำนวณเงินเดือนรายปีรวมกับโบนัส
        return (self.salary * 12) + self.bonus # คืนค่าจำนวนเงินเดือนรายปีบวกกับโบนัส

class Developer(Employee): # คลาส Developer สืบทอดคุณสมบัติและพฤติกรรมจากคลาส Employee
    def __init__(self, name, salary, projects): # กำหนดชื่อ, เงินเดือน, และจำนวนโครงการที่นักพัฒนาทำ
        super().__init__(name, salary) # เรียกใช้งานฟังก์ชัน __init__ ของคลาส Employee
        self.projects = projects # กำหนดค่าจำนวนโครงการที่รับมาให้กับคุณสมบัติ projects ของออบเจ็กต์

    def annual_salary(self): # ฟังก์ชันคำนวณเงินเดือนรายปีรวมกับค่าตอบแทนจากโครงการ
        base_salary = self.salary * 12 # คำนวณเงินเดือนรายปีพื้นฐาน (เงินเดือน * 12 เดือน)
        return base_salary + (self.projects * 1000) # คืนค่าจำนวนเงินเดือนรายปีรวมกับค่าตอบแทนจากโครงการ (1000 หน่วยต่อโครงการ)

# สร้างออบเจ็กต์ manager ของคลาส Manager โดยกำหนดชื่อเป็น "Alice", เงินเดือน 6000 หน่วย, และโบนัส 5000 หน่วย
manager = Manager("Alice", 6000, 5000) 

# สร้างออบเจ็กต์ developer ของคลาส Developer โดยกำหนดชื่อเป็น "Bob", เงินเดือน 5000 หน่วย, และจำนวนโครงการ 3 โครงการ
developer = Developer("Bob", 5000, 3) 

# คำนวณเงินเดือนรายปีรวมของผู้จัดการและนักพัฒนา
total_annual_salary = manager.annual_salary() + developer.annual_salary() 

# แสดงผลรวมเงินเดือนรายปีของผู้จัดการและนักพัฒนา
print(total_annual_salary)
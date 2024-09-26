import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("เครื่องคิดเลข")
        
        # ตั้งค่าสีพื้นหลังของหน้าต่างหลัก
        master.configure(bg='black')

        # วิดเจ็ต Entry เพื่อแสดงการคำนวณพร้อมกรอบสีน้ำเงิน
        self.display = tk.Entry(master, width=16, font=('Arial', 32), borderwidth=2, relief='ridge', bg='white', fg='black', highlightbackground='blue', highlightcolor='blue', highlightthickness=2)
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=10, sticky='nsew')

        # ตั้งค่า grid เพื่อให้ปุ่มขยายอย่างเท่าเทียมกัน
        for i in range(7):
            master.grid_rowconfigure(i, weight=1)
            master.grid_columnconfigure(i, weight=1)

        # การจัดวางปุ่ม
        buttons = [
            ('AC', 1, 0, 'lightgray', 'black'), ('+/-', 1, 1, 'lightgray', 'black'), ('%', 1, 2, 'lightgray', 'black'), ('←', 1, 3, 'lightgray', 'black'),
            ('(', 2, 0, 'gray', 'black'), (')', 2, 1, 'gray', 'black'), ('×', 2, 2, 'gray', 'orange'), ('÷', 2, 3, 'gray', 'orange'),
            ('7', 3, 0, 'gray', 'white'), ('8', 3, 1, 'gray', 'white'), ('9', 3, 2, 'gray', 'white'), ('-', 3, 3, 'gray', 'orange'),
            ('4', 4, 0, 'gray', 'white'), ('5', 4, 1, 'gray', 'white'), ('6', 4, 2, 'gray', 'white'), ('+', 4, 3, 'gray', 'orange'),
            ('1', 5, 0, 'gray', 'white'), ('2', 5, 1, 'gray', 'white'), ('3', 5, 2, 'gray', 'white'), ('=', 5, 3, 'gray', 'orange', 1, 2),
            ('0', 6, 0, 'gray', 'white', 2), ('.', 6, 2, 'gray', 'orange')
        ]

        for (text, row, col, bg_color, fg_color, *span) in buttons:
            if text == '+/-':
                self.add_canvas_button(text, row, col, bg_color, fg_color, span)
            else:
                self.add_button(text, row, col, bg_color, fg_color, span)

    def add_button(self, text, row, col, bg_color, fg_color, span, border_color=None):
        button = tk.Button(self.master, text=text, font=('Arial', 18), width=5, height=2,
                           command=lambda t=text: self.on_button_click(t), bg=bg_color, fg=fg_color, borderwidth=2, relief='solid')
        if border_color:
            button.config(highlightbackground=border_color, highlightcolor=border_color, highlightthickness=2)
        columnspan = span[0] if len(span) > 0 else 1
        rowspan = span[1] if len(span) > 1 else 1
        button.grid(row=row, column=col, columnspan=columnspan, rowspan=rowspan, sticky='nsew', padx=5, pady=5)

    def add_canvas_button(self, text, row, col, bg_color, fg_color, span):
        canvas = tk.Canvas(self.master, width=90, height=80, bg=bg_color, highlightthickness=0)
        canvas.create_rectangle(5, 5, 94, 75, outline='orange', width=2)
        button = tk.Button(canvas, text=text, font=('Arial', 18), width=4, height=2,
                           command=lambda t=text: self.on_button_click(t), bg=bg_color, fg=fg_color, borderwidth=0)
        canvas.create_window(49, 40, window=button)
        columnspan = span[0] if len(span) > 0 else 1
        rowspan = span[1] if len(span) > 1 else 1
        canvas.grid(row=row, column=col, columnspan=columnspan, rowspan=rowspan, sticky='nsew', padx=5, pady=5)

    def on_button_click(self, char):
        if char == 'AC':
            self.display.delete(0, tk.END)
        elif char == '=':
            self.calculate()
        elif char == '+/-':
            self.change_sign()
        elif char == '←':
            self.backspace()
        else:
            self.display.insert(tk.END, char)

    def calculate(self):
        try:
            result = eval(self.display.get().replace('÷', '/').replace('×', '*'))
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(result))
        except Exception:
            self.display.delete(0, tk.END)
            self.display.insert(0, 'Error')

    def change_sign(self):
        try:
            current_value = self.display.get()
            if current_value.startswith('-'):
                self.display.delete(0)
                self.display.insert(0, current_value[1:])
            else:
                self.display.delete(0)
                self.display.insert(0, '-' + current_value)
        except ValueError:
            pass

    def backspace(self):
        current_text = self.display.get()
        new_text = current_text[:-1]
        self.display.delete(0, tk.END)
        self.display.insert(0, new_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()

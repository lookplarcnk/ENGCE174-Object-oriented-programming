import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        
        # Set the background color of the main window
        master.configure(bg='black')

        # Entry widget to show calculations
        self.display = tk.Entry(master, width=16, font=('Arial', 24), borderwidth=2, relief='ridge', bg='white', fg='black')
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # Buttons layout
        buttons = [
            ('AC', 1, 0, 'lightgray'), ('+/-', 1, 1, 'lightgray'), ('%', 1, 2, 'lightgray'), ('←', 1, 3, 'lightgray'),
            ('7', 2, 0, 'gray'), ('8', 2, 1, 'gray'), ('9', 2, 2, 'gray'), ('/', 2, 3, 'orange'),
            ('4', 3, 0, 'gray'), ('5', 3, 1, 'gray'), ('6', 3, 2, 'gray'), ('*', 3, 3, 'orange'),
            ('1', 4, 0, 'gray'), ('2', 4, 1, 'gray'), ('3', 4, 2, 'gray'), ('-', 4, 3, 'orange'),
            ('0', 5, 0, 'gray'), ('.', 5, 1, 'gray'), ('(', 5, 2, 'lightgray'), (')', 5, 3, 'lightgray'),
            ('+', 6, 3, 'orange'), ('=', 6, 2, 'orange')  # Move "+" to row 6 under "-"
        ]

        for (text, row, col, color) in buttons:
            self.add_button(text, row, col, color)

    def add_button(self, text, row, col, color):
        button = tk.Button(self.master, text=text, font=('Arial', 18), width=4, height=2,
                           command=lambda t=text: self.on_button_click(t), bg=color, fg='white')
        button.grid(row=row, column=col, sticky='nsew', padx=5, pady=5)

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
            self.display.insert(tk.END, 'Error')

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

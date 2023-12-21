import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("MAYORAL CALCULATOR")

        self.entry = tk.Entry(root , font=("Helvetica" , 16))
        self.entry.grid(row=0 , column=0 , columnspan=4)

        self.create_buttons()

    def create_buttons(self):
        buttons=[
            ('7' , 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4' , 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1' , 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0' , 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C',5, 0),

        ]

        
        for (text, row, col) in buttons:
            button = tk.Button(self.root, text=text, font=("Helvetica", 16), command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=10, pady=10)

    def on_button_click(self, char):
        if char == '=':
            try:
                result = eval(self.entry.get())
                self.entry.delete(0,tk.END)
                self.entry.insert(tk.END, result)
            except:
                self.entry.delete(0,tk.END)
                self.entry.insert(tk.END, "error")
        elif char == 'C':
            self.entry.delete(0, tk.END)

        else:
            self.entry.insert(tk.END, char)



if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()

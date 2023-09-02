import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_add():
    first_number = entry.get()
    global f_num
    global math_operation
    math_operation = "addition"
    f_num = int(first_number)
    entry.delete(0, tk.END)

def button_subtract():
    first_number = entry.get()
    global f_num
    global math_operation
    math_operation = "subtraction"
    f_num = int(first_number)
    entry.delete(0, tk.END)

def button_equal():
    second_number = entry.get()
    entry.delete(0, tk.END)
    if math_operation == "addition":
        entry.insert(tk.END, f_num + int(second_number))
    elif math_operation == "subtraction":
        entry.insert(tk.END, f_num - int(second_number))

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create an entry widget to display the result
entry = tk.Entry(window, width=20)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Define the number buttons
buttons = [
    "7", "8", "9",
    "4", "5", "6",
    "1", "2", "3",
    "0"
]

row = 1
col = 0

for button in buttons:
    btn = tk.Button(window, text=button, padx=10, pady=10, command=lambda num=button: button_click(num))
    btn.grid(row=row, column=col)
    col += 1
    if col > 2:
        col = 0
        row += 1

# Define operator buttons
button_add = tk.Button(window, text="+", padx=10, pady=10, command=button_add)
button_add.grid(row=row, column=col)
col += 1

button_subtract = tk.Button(window, text="-", padx=10, pady=10, command=button_subtract)
button_subtract.grid(row=row, column=col)
col += 1

# Define additional buttons
button_clear = tk.Button(window, text="C", padx=10, pady=10, command=button_clear)
button_clear.grid(row=row, column=col)
col += 1

button_equal = tk.Button(window, text="=", padx=10, pady=10, command=button_equal)
button_equal.grid(row=row, column=col)

# Start the main event loop
window.mainloop()

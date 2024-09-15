import tkinter as tk


def on_button_click(value):
    current = display.get()
    if value == "=":
        try:
            result = str(eval(current))
            display.delete(0, tk.END)
            display.insert(tk.END, result)
        except Exception as e:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
    elif value == "C":
        display.delete(0, tk.END)
    elif value == "%":
        try:
            result = str(eval(current) / 100)
            display.delete(0, tk.END)
            display.insert(tk.END, result)
        except Exception as e:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
    else:
        display.insert(tk.END, value)

root = tk.Tk()
root.title("Calculator")


display = tk.Entry(root, width=35, borderwidth=5)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Buttons
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "%", "+",
    "C", "=", "", ""
]

row = 1
col = 0
for button in buttons:
    if button != "":
        tk.Button(root, text=button, width=9, height=3, command=lambda b=button: on_button_click(b)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()

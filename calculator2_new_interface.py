import tkinter as tk

# Global variable to store the expression
expression = ""

def on_button_click(digit):
    global expression
    expression += str(digit)
    
    # Update the text field with the current expression
    text_result.delete("1.0", tk.END)
    text_result.insert("1.0", expression)
    
    # Check if the expression should be evaluated
    if digit == '=':
        try:
            result = str(eval(expression[:-1]))  # Evaluate the expression without the '='
            text_result.delete("1.0", tk.END)
            text_result.insert("1.0", result)
            expression = result  # Reset the expression to the result
        except Exception as e:
            text_result.delete("1.0", tk.END)
            text_result.insert("1.0", "Error")
            expression = ""  # Reset the expression on error

root = tk.Tk()

root.title("Basic Tkinter Window")
root.geometry("300x275")

text_result = tk.Text(root, height=2, width=30)
text_result.grid(columnspan=5)

# Digit buttons
btn1 = tk.Button(root, text="1", command=lambda: on_button_click(1), width=4)
btn1.grid(column=1, row=1)

btn2 = tk.Button(root, text="2", command=lambda: on_button_click(2), width=4)
btn2.grid(column=2, row=1)

btn3 = tk.Button(root, text="3", command=lambda: on_button_click(3), width=4)
btn3.grid(column=1, row=2)

btn4 = tk.Button(root, text="4", command=lambda: on_button_click(4), width=4)
btn4.grid(column=2, row=2)

btn5 = tk.Button(root, text="5", command=lambda: on_button_click(5), width=4)
btn5.grid(column=1, row=3)

btn6 = tk.Button(root, text="6", command=lambda: on_button_click(6), width=4)
btn6.grid(column=2, row=3)

btn7 = tk.Button(root, text="7", command=lambda: on_button_click(7), width=4)
btn7.grid(column=3, row=3)

btn8 = tk.Button(root, text="8", command=lambda: on_button_click(8), width=4)
btn8.grid(column=1, row=4)

btn9 = tk.Button(root, text="9", command=lambda: on_button_click(9), width=4)
btn9.grid(column=2, row=4)

btn0 = tk.Button(root, text="0", command=lambda: on_button_click(0), width=4)
btn0.grid(column=3, row=4)

btn_plus = tk.Button(root, text="+", command=lambda: on_button_click("+"), width=4)
btn_plus.grid(column=3, row=1)

btn_min = tk.Button(root, text="-", command=lambda: on_button_click("-"), width=4)
btn_min.grid(column=4, row=2)

btn_mult = tk.Button(root, text="*", command=lambda: on_button_click("*"), width=4)
btn_mult.grid(column=3, row=2)

btn_dev = tk.Button(root, text="/", command=lambda: on_button_click("/"), width=4)
btn_dev.grid(column=4, row=3)

btn_equal = tk.Button(root, text="=", command=lambda: on_button_click("="), width=4)
btn_equal.grid(column=4, row=1)
root.mainloop()

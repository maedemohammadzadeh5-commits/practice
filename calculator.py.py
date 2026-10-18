import tkinter as tk

# 🎨 رنگ‌های پاستیلی
COLORS = {
    "bg": "#fff9fb",        # پس‌زمینه کلی
    "display_bg": "#fffaf0", # پس‌زمینه نمایشگر
    "button_bg": "#c8f7c5",  # رنگ دکمه اعداد
    "operator_bg": "#b2dffb",# رنگ دکمه عملگرها
    "clear_bg": "#fcbad3",   # رنگ پاک‌کردن
    "text": "#444444"        # متن
}

root = tk.Tk()
root.title("ماشین حساب پاستیلی ساده ")
root.config(bg=COLORS["bg"])
root.geometry("280x370")
root.resizable(False, False)

expression = ""
input_text = tk.StringVar()

def press(item):
    global expression
    expression += str(item)
    input_text.set(expression)

def equal():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = result
    except:
        input_text.set("خطا")
        expression = ""

def clear():
    global expression
    expression = ""
    input_text.set("")

# نمایشگر
entry = tk.Entry(root, textvariable=input_text, font=('Arial', 24),
                 bg=COLORS["display_bg"], fg=COLORS["text"], bd=0, justify='right')
entry.pack(ipady=15, padx=10, pady=20, fill="x")

# دکمه‌ها
buttons = [
    ['7','8','9','/'],
    ['4','5','6','*'],
    ['1','2','3','-'],
    ['0', '=', '+']
]

for row_values in buttons:
    row = tk.Frame(root, bg=COLORS["bg"])
    row.pack(expand=True, fill="both")
    for value in row_values:
        if value in ['+','-','*','/','=']:
            bg_color = COLORS["operator_bg"]
        else:
            bg_color = COLORS["button_bg"]
        btn = tk.Button(row, text=value, font=('Arial', 18),
                        bg=bg_color, fg=COLORS["text"], width=5, height=2, bd=0,
                        command=lambda v=value: equal() if v=='=' else press(v))
        btn.pack(side="left", expand=True, fill="both", padx=2, pady=2)

# دکمه پاک کردن
clear_btn = tk.Button(root, text="پاک کردن", font=('Arial', 16),
                      bg=COLORS["clear_bg"], fg=COLORS["text"],
                      command=clear, bd=0, width=15)
clear_btn.pack(pady=10)

root.mainloop()

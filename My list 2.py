import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

root = tk.Tk()
root.title("modern to do list😎")
root.geometry("550x650")
# رنگ پس‌زمینه اصلی را به یک رنگ مناسب‌تر تغییر دادم، رنگ قبلی خیلی روشن بود.
# همچنین می‌توانید از رنگ اصلی خودتان استفاده کنید: root.configure(bg="#ec0b7c")
root.configure(bg="#f0f0f0") # رنگ خاکستری روشن

style = ttk.Style()
# theme_use("calm") ممکن است در همه جا در دسترس نباشد، از یک تم پیش‌فرض استفاده می‌کنیم.
# style.theme_use("calm")
style.configure("TButton",
                font=("Arial", 10, "bold"), # فونت را به Arial تغییر دادم تا سازگارتر باشد
                padding=6)
style.configure("TEntry",
                padding=5)

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, "☐ " + task) # یک فاصله بین تیک و متن اضافه کردم
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("warning", "Enter task😣")

def delete_task():
    # curselection() یک tuple برمی‌گرداند، اگر خالی نباشد، اولین عنصر را می‌گیریم
    selected_indices = listbox.curselection()
    if selected_indices:
        # برای حذف کردن چندین آیتم انتخاب شده، بهتر است از آخر به اول حذف کنیم
        # تا ایندکس‌ها به هم نریزند.
        for index in selected_indices[::-1]:
            listbox.delete(index)

def toggle_done():
    selected_indices = listbox.curselection()
    if selected_indices:
        index = selected_indices[0] # فقط اولین آیتم انتخاب شده را در نظر می‌گیریم
        text = listbox.get(index)

        # از startswith استفاده می‌کنیم و فاصله را هم در نظر می‌گیریم
        if text.startswith("☐ "):
            # replace را برای جایگزینی "☐ " با "✓ " استفاده می‌کنیم
            new_text = text.replace("☐ ", "✓ ", 1)
        elif text.startswith("✓ "):
             # replace را برای جایگزینی "✓ " با "☐ " استفاده می‌کنیم
            new_text = text.replace("✓ ", "☐ ", 1)
        else:
            # اگر هیچکدام از علامت‌ها در ابتدا نبود، تغییری نمی‌دهیم
            return

        listbox.delete(index)
        listbox.insert(index, new_text)


# --- عنوان ---
title = tk.Label(root,
               text="MY TO DO LIST 🤗",
               bg="#b319ab", # رنگ پس‌زمینه عنوان
               fg="white",
               font=("Arial", 19, "bold"))
# اشتباه: title.pack=15 باید title.pack(pady=15) باشد
title.pack(pady=15)

# --- فریم ورودی ---
# اشتباه: tk.frame باید tk.Frame باشد
input_frame = tk.Frame(root, bg="#d488c8") # رنگ پس‌زمینه فریم ورودی
input_frame.pack()

entry = ttk.Entry(input_frame, width=25)
entry.pack(side="left", padx=5)

add_btn = ttk.Button(input_frame, text="Add", command=add_task)
add_btn.pack(side="left")

# --- لیست باکس ---
# اشتباه: tk.listbox باید tk.Listbox باشد
listbox = tk.Listbox(root,
                     width=40,
                     height=15,
                     font=("Arial", 12),
                     bg="#47d6f0", # رنگ پس‌زمینه لیست باکس
                     fg="white",
                     selectbackground="#5be288", # رنگ پس‌زمینه آیتم انتخاب شده
                     bd=0, # ضخامت حاشیه
                     highlightthickness=0) # ضخامت حاشیه هایلایت
listbox.pack(pady=20)

# --- فریم دکمه‌ها ---
# اشتباه: tk.Frame باید tk.Frame باشد
btn_frame = tk.Frame(root, bg="#cafa7c") # رنگ پس‌زمینه فریم دکمه‌ها
btn_frame.pack()

# اشتباه: toggel_done باید toggle_done باشد
done_btn = ttk.Button(btn_frame, text="Toggle Done ✔", command=toggle_done)
done_btn.pack(side="left", padx=5)

delete_btn = ttk.Button(btn_frame, text="Delete", command=delete_task)
delete_btn.pack(side="left", padx=5)

root.mainloop()

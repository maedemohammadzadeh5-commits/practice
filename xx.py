import tkinter as tk

def divide():
    a = float(num1.get())
    b = float(num2.get())
    result.config(text=a / b)

def check():
    if num2.get() == "0":
        div.config(state="disabled")
    else:
        div.config(state="normal")

window = tk.Tk()
window.title("ماشین حساب")
window.geometry("300x250")

tk.Label(window, text="عدد اول").pack()
num1 = tk.Entry(window)
num1.pack()

tk.Label(window, text="عدد دوم").pack()
num2 = tk.Entry(window)
num2.pack()

num2.bind("<KeyRelease>", lambda e: check())

tk.Button(window, text="+", command=lambda: result.config(
    text=float(num1.get()) + float(num2.get()))).pack()

tk.Button(window, text="-", command=lambda: result.config(
    text=float(num1.get()) - float(num2.get()))).pack()

div = tk.Button(window, text="÷", command=divide)
div.pack()

result = tk.Label(window, text="نتیجه")
result.pack(pady=10)

tk.Button(window, text="Exit", command=window.destroy).pack()

window.mainloop()




#import  xml.etree.ElementTree as ET
#tree=ET.parse("students.xml")
#root=tree.getroot()

#for student in root.findall("student"):
    #name=student.find("name").text
   # score=student.find("score").text

   # print(name,score)

def show_player():
    file = open("players.txt", "r")
    print("\n------لیست بازیکن------\n")
    for line in file:
        line = line.strip()
        if not line:
            continue
        parts = line.split(",")
        if len(parts) == 3:
            name, score, level = parts
            print("نام:", name)
            print("امتیاز:", score)
            print("مرحله:", level)
            print("------------------")
    file.close()

def search_player():
    target = input("نام بازیکن را وارد کنید :")
    file = open("players.txt", "r")
    found = False
    for line in file:
        line = line.strip()
        if not line:
            continue
        parts = line.split(",")
        if len(parts) == 3:
            name, score, level = parts
            if name.lower() == target.lower():
                print("\nبازیکن پیدا شد.")
                print("امتیاز:", score)
                print("مرحله:", level)
                found = True
                break
    if found == False:
        print("بازیکن با این نام وجود ندارد:")
    file.close()

def add_player():
    name = input("نام بازیکن:")
    score = input("امتیاز بازیکن:")
    level = input("مرحله بازیکن:")
    file = open("players.txt", "a")
    file.write(f"{name},{score},{level}\n")
    file.close()
    print("بازیکن با موفقیت ذخیره شد .")

def best_player():
    file = open("players.txt", "r")
    best_name = ""
    best_score = -1
    best_level = ""
    for line in file:
        line = line.strip()
        if not line:
            continue
        parts = line.split(",")
        if len(parts) == 3:
            name, score, level = parts
            score = int(score)
            if score > best_score:
                best_score = score
                best_name = name
                best_level = level
    file.close()
    print("\nبهترین بازیکن")
    print("نام:", best_name)
    print("امتیاز:", best_score)
    print("مرحله:", best_level)

def pro_players():
    file = open("players.txt", "r")
    print("\nبازیکنان حرفه ای :\n")
    for line in file:
        line = line.strip()
        if not line:
            continue
        parts = line.split(",")
        if len(parts) == 3:
            name, score, level = parts
            level = int(level)
            if level > 5:
                print(name)
    file.close()

while True:
    print("\n-----------------------")
    print("    سیستم مدیریت بازی ")
    print("----------------------")
    print("1-نمایش بازیکنان ")
    print("2-جستجوی بازیکن ")
    print("3- افزودن بازیکن")
    print("4-بهترین بازیکن")
    print("5-بازیکنان حرفه ای")
    print("0-خروج")
    print("-----------------------")
    
    choice = input("انتخاب شما :")

    if choice == "1":
        show_player()
    elif choice == "2":
        search_player()
    elif choice == "3":
        add_player()
    elif choice == "4":
        best_player()
    elif choice == "5":
        pro_players()
    elif choice == "0":
        print("خداحافظ")
        break
    else:
        print("گزینه وارد شده معتبر نیست .")

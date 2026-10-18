#دو برابر کردن اعداد
def double(x):
    return x * 2

numbers = [1, 2, 3, 4]

result = map(double, numbers)

print(list(result))


#محاسبه مربع اعداد
def square(x):
    return x ** 2

numbers = [2,3,4,5]

result = map(square, numbers)

print(list(result))

#تبدیل رشته‌ها به حروف بزرگ
def upper_word(word):
    return word.upper()

names = ["ali", "sara", "python"]

result = map(upper_word, names)

print(list(result))

#محاسبه طول کلمات
def word_length(word):
    return len(word)

words = ["cat", "elephant", "book"]

result = map(word_length, words)

print(list(result))

#تبدیل عدد به رشته
def convert(number):
    return str(number)

numbers = [10,20,30]

result = map(convert, numbers)

print(list(result))

#6: محاسبه قیمت کالاها پس از اعمال مالیات
def add_tax(price):
    return price * 1.10

prices = [100, 250, 80, 150, 300]

new_prices = map(add_tax, prices)

print(list(new_prices))

#7: تبدیل نمرات از ۲۰ به ۱۰۰
def convert(score):
    return score * 5

scores = [12, 15, 18, 20, 9]

new_scores = map(convert, scores)

print(list(new_scores))
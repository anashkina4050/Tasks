# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь
# Если трехзначное число разделить на 100 без остатка, то получим первую цифру этого числа

n = int(input("Введите трехзначное число: "))
num1 = n // 100
num2 = n % 100 // 10
num3 = n % 10
print("Сумма цифр: ", num1 + num2 + num3)
print("Произведение цифр: ", num1 * num2 * num3)

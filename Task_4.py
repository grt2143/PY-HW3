# Напишите программу, которая будет преобразовывать десятичное число в двоичное. 
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10


rem = ""
num = int(input("Введите число для преобразовывания десятичного числа в двоичное: "))
while num != 0:
    rem = str(num % 2) + rem
    num //= 2
print(rem)
# 4. Пользователь вводит две буквы.
# Определить, на каких местах алфавита они стоят,
# и сколько между ними находится букв.

first = input("1-я буква: ")
second = input("2-я буква: ")

first = ord(first) - ord("a") + 1
second = ord(second) - ord("a") + 1

print(f"Порядковый номер 1-й буквы = {first}, 2-й = {second}")
print(f"Число букв между введенными: {abs(first - second) - 1}")

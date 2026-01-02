from random import randint

# Генерируем число и счетчик для попыток
number = randint(1, 100)
attempts = 0

print("Добро пожаловать в числовую угадайку! Let's fun!")

# Защита от дурака: проверка числа на корректность
def is_valid(text):
    return 0 <= int(text) <= 100

while True:
    print("Введите число от 1 до 100:")
    num = input()

    if is_valid(num):
        num = int(num)
        if num == number:
            attempts += 1
            print(f"Вы угадали! Congratulations!\nКоличество попыток угадать число: {attempts}")
            print("Сыграем еще разок? д - да, н - нет")
            answer = input()
            if answer.lower() == "д":
                continue
            elif answer.lower() == 'н':
                print("Спасибо, что играли в угадайку! До скорых встреч...")
                break
            else:
                print("Извините, не понял вас. Тогда продолжаем игру!")
        elif num < number:
            attempts += 1
            print("Ваше число меньше загаданного, попробуйте еще разок!")
        elif num > number:
            attempts += 1
            print("Ваше число больше загаданного, попробуйте еще разок!")

    else:
        print("А может быть все-таки введем целое число от 1 до 100?")
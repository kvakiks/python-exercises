from random import randint

while True:
    flag = True

    print("Добро пожаловать в числовую угадайку!")
    print("Введите предельное число, чтобы я загадал случайное:")

    while True:
        border = input()
        if border.isdigit():
            border = int(border)

            # Генерируем число
            number = randint(1, border)
            break
        else:
            print("Должно быть число.")
            continue


    # Защита от дурака: проверка числа на корректность
    def is_valid(text):
        if not text.isdigit():
            return False
        return 0 <= int(text) <= border


    #  Счетчик для попыток
    attempts = 0

    while True:
        print(f"Введите число от 1 до {border}:")
        num = input()

        if is_valid(num):
            num = int(num)
            if number == num:
                attempts += 1
                print(f"Вы угадали! Congratulations!\nКоличество попыток угадать число: {attempts}")
                print("Сыграем еще разок? д - да, н - нет")
                answer = input()
                if answer.lower() == "д":
                    break
                elif answer.lower() == 'н':
                    print("Спасибо, что играли в угадайку! До скорых встреч...")
                    flag = False
                    break
                else:
                    print("Извините, не понял вас. Тогда продолжаем игру!")
                    break
            elif num < number:
                attempts += 1
                print("Больше.")
            elif num > number:
                attempts += 1
                print("Меньше.")

        else:
            print(f"А может быть все-таки введем целое число от 1 до {border}?")

    if not flag:
        break
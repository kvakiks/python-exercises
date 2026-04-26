# import random
from time import sleep

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

while True:
    print(f'Привет! Давай соберем твой идеальный пароль.\nПара вопросов:')
    sleep(1)
    print(f'Сколько паролей я должен сгенерировать?')
    qual = int(input())

    print(f'Длина пароля должна быть...')
    length = int(input())

    print(f'Включать ли цифры {digits}?')
    answer = input().lower()

    print(f'Включать ли прописные буквы {uppercase_letters}?')
    answer2 = input().lower()

    print(f'Включать ли строчные буквы {lowercase_letters}?')
    answer3 = input().lower()

    print(f'Включать ли символы {punctuation}?')
    answer4 = input().lower()

    print(f'Исключать ли неоднозначные символы "il1Lo0O?"')
    answer5 = input().lower()
import random
gener_number = random.randint (1,99)
user_number = ''
while user_number != gener_number:
    user_number = int(input ('Угадайте число: '))
    if user_number < gener_number:
        print ('Ваше число меньше выиграшного значения.')
    elif user_number > gener_number:
        print ('Ваше число больше выиграшного значения.')
    else:
        print ('Выиграшное число: ', gener_number)
        print ('Число пользователя: ', user_number)
        print ('Поздравляю! Вы угадали число!')

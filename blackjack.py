from random import shuffle

deck = [6, 7, 8, 9, 10, 2, 3, 4, 11] * 4
shuffle(deck)

print('Поиграем в blackjack?')
count = 0

while True:
    choice = input('Будете брать карту? y/n\n')
    if choice.lower() in ['y', 'д', 'yes', 'да']:
        current = deck.pop()
        print(f'Вам попалась карта достоинством {current}')
        count += current
        if count > 21:
            print('Извините, но вы проиграли')
            break
        elif count == 21:
            print('Поздравляю, вы набрали 21!')
            break
        else:
            print(f'У вас {count} очков')
    elif choice.lower() in ['n', 'н', 'no', 'нет']:
        print('У вас {count} очков и вы закончили игру')
        break

print('Спасибо за игру!\nДо новых втреч!')
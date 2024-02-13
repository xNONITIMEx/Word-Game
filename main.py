import random as rnd
from words import get_words, find_word

all_words = get_words()
words = get_words()
used = []
letter = ''


def my_turn(user_word):
    global words
    global used
    letter = user_word.strip()[-1] if user_word.strip()[-1] not in 'ьыъ' else user_word.strip()[-2]
    if len(words[letter]) == 0:
        print('Я проиграл, поздравляю с победой!')
        return None
    my_word = rnd.choice(words[letter])
    words[letter].remove(my_word)
    used.append(my_word)
    print(f'Мое слово: {my_word}')
    letter = my_word[-1]
    return letter


while True:
    user_word = input('Ведите слово: ').lower()
    if user_word == '!':
        break
    if len(used) == 0:
        used.append(user_word)
        if user_word in words[user_word[0]]:
            words[user_word[0]].remove(user_word)
        if my_turn(user_word) is None:
            break
    else:
        if user_word in used:
            print('Такое слово уже было')
            continue
        if user_word[0] != letter and letter != '':
            print(f'Нужно слово на последнюю букву моего слова -- {letter}')
            continue
        if not find_word(user_word):
            print('Такого слова не существует у меня в словаре! Введите другое.')
            continue
        if my_turn(user_word) is None:
            break

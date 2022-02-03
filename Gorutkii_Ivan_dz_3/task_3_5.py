from random import choice, choices

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
full_list = list(zip(nouns, adverbs, adjectives))


def get_jokes(count: int) -> list:
    """Возвращает список шуток в количестве count"""
    list_out = []

    for i in range(count):
        noun_ = choice(nouns)
        adverb_ = choice(adverbs)
        adjective_ = choice(adjectives)
        funny_ = f"{noun_} {adverb_} {adjective_}"
        list_out.append(funny_)

    return list_out


def get_jokes_adv(count: int, flag: bool=True) -> list:
    """Возвращает список шуток в количестве count в зависимости от флага"""
    list_out = []
    repeat_funs = []
    if flag:
        return get_jokes(count)
    else:
        i = 0
        funny = ''
        finish = True
        u = 0
        # составляем шутку из разных слов
        while finish:
            word = choice(choice(full_list))
            # проверяем использовалась ли слово повторно. если нет, составляем шутку
            if word not in repeat_funs:
                funny += f'{word} '
                repeat_funs.append(word)
                i += 1
                if i % 3 == 0:
                    list_out.append(funny.rstrip())
                    funny = ''
                elif len(list_out) == count: finish = False
            elif len(list_out) == count or\
                len(list_out) == len(full_list): finish = False

    return list_out

# def make_up_funny(word: str):

# print(get_jokes(2))
# print(get_jokes(10))
print(get_jokes_adv(12, False))
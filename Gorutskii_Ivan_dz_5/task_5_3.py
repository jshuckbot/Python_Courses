import typing

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']


def check_gen(tutors: list, klasses: list):
    """реализация генератора, возвращающий кортежи вида (<tutor>, <klass>)"""
    for _ in range(len(tutors)):
        if _ < len(klasses):
            yield tutors[_], klasses[_]
        else:
            yield tutors[_], None


generator = check_gen(tutors, klasses)
# добавьте здесь доказательство, что создали именно генератор 
print(generator)
for _ in range(len(tutors)):
    print(next(generator))
next(generator)  # если раскомментировать, то должно падать в traceback по StopIteration

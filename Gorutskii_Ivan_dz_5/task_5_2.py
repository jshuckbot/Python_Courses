n = 15
generator = (_ for _ in range(1, n+1, 2))

for _ in range(1, n+1, 2):
    print(next(generator))
next(generator)  # если раскомментировать, то должно падать в traceback по StopIteration

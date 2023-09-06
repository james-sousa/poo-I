def lista(n):
    for l in n:
        if isinstance(l, list):
            lista(l)
        else:
            print(l)


n = [0, 1, [2, [3, 4]], 5]

lista(n)


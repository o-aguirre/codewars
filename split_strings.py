def solution(s):
    lista = []

    if len(s) == 1:
        s += '_'
    if len(s) % 2 != 0:
        s += '_'
    for i in range(len(s)):
        if i % 2 != 0:
            lista.append(s[i - 1] + s[i])

    return lista
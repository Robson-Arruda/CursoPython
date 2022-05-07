lista = [
    ['P1', 49],
    ['P2', 15],
    ['P3', 11],
    ['P4', 17],
    ['P5', 13],
    ['P6', 8],
    ['P7', 40]
]

# lista.sort(key=lambda item: item[1])
print(sorted(lista, key=lambda i: i[1], reverse=True))
print(lista)

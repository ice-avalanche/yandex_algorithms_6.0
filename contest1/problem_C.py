from itertools import groupby

n = int(input())
rows = []

for i in range(n):
    rows.append(input())

if ''.join(rows).count('#') == n*n:
    print("I")
elif ''.join(rows).count('.') == n*n:
    print("X")
else:
    rows = list(map(lambda x: x[0], groupby(rows)))

    if rows[0].count('.') == len(rows[0]):
        rows.pop(0)
    if rows[-1].count('.') == len(rows[-1]):
        rows.pop()

    cols = [''.join(row) for row in zip(*rows)]
    cols = list(map(lambda x: x[0], groupby(cols)))

    if cols[0].count('.') == len(cols[0]):
        cols.pop(0)
    if cols[-1].count('.') == len(cols[-1]):
        cols.pop()

    rows = [''.join(row) for row in zip(*cols)]

    match rows:
        case ["#"]:
            print("I")
        case ["##", "#.", "##"]:
            print("C")
        case ["###", "#.#", "###"]:
            print("O")
        case ["#.", "##"]:
            print("L")
        case ["#.#","###","#.#"]:
            print("H")
        case ["###","#.#","###","#.."]:
            print("P")
        case _:
            print("X")

def get_size_and_survpoint(dict):
    size = [dict[item][0] for item in dict]
    survpoint = [dict[item][1] for item in dict]
    return size, survpoint


def get_memtable(dict, A=9):
    size, survpoint = get_size_and_survpoint(dict)
    n = len(survpoint)
    V = [[0 for a in range(A + 1)] for i in range(n + 1)]

    for i in range(n + 1):
        for a in range(A + 1):
            if i == 0 or a == 0:
                V[i][a] = 0
            elif size[i - 1] <= a:
                V[i][a] = max(survpoint[i - 1] + V[i - 1][a - size[i - 1]], V[i - 1][a])
            else:
                V[i][a] = V[i - 1][a]
    return V, size, survpoint


def get_selected_items_list(dict, A=9):
    V, size, survpoint = get_memtable(dict)
    n = len(survpoint)
    res = V[n][A]
    a = A
    items_list = []

    for i in range(n, 0, -1):
        if res <= 0:
            break
        if res == V[i - 1][a]:
            continue
        else:
            items_list.append((size[i - 1], survpoint[i - 1]))
            res -= survpoint[i - 1]
            a -= size[i - 1]

    selected_stuff = []
    summa = 10

    for search in items_list:
        for key, value in dict.items():
            if value == search and key not in selected_stuff:
                for i in range(value[0]):
                    selected_stuff.append(key)
                break

    return selected_stuff


def total_value(stuff):
    summa = 10
    for key, value in dict.items():
        if key in stuff:
            summa += value[1] * (stuff.count(key) // value[0])
        else:
            summa -= value[1]
    return summa


dict = {'r': (3, 25),
        'p': (2, 15),
        'a': (2, 15),
        'm': (2, 20),
        'i': (1, 5),
        'k': (1, 15),
        'x': (3, 20),
        't': (1, 25),
        'f': (1, 15),
        'd': (1, 10),
        's': (2, 20),
        'c': (2, 20)
        }

stuff = get_selected_items_list(dict)
for i in range(3):
    print(', '.join(stuff[3 * i: 3 * (i + 1)]))

print(f"Итоговые очки выживания: {total_value(stuff)}")

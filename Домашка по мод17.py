array = list(map(int, input("Введите последовательность чисел:").split()))

for i in range(len(array)):
    idx_min = i
    for j in range(i, len(array)):
        if array[j] < array[idx_min]:
            idx_min = j
    if i != idx_min:
        array[i], array[idx_min] = array[idx_min], array[i]

print(array)

num = int(input("Введите любое число:"))

def binary_search(array, num, left, right):
    try:
        if left > right:
            return False
        middle = (right + left) // 2
        if array[middle] == num:
            return middle
        elif num < array[middle]:
            return binary_search(array, num, left, middle - 1)
        else:
            return binary_search(array, num, middle + 1, right)
    except IndexError:
        return 'Число выходит за диапазон списка, введите меньшее число.'


if not binary_search(array, num, 0, len(array)):
    rI = min(array, key=lambda x: (abs(x - num), x))
    index = array.index(rI)
    max_index = index + 1
    min_index = index - 1

    if rI < num:
        print(f'''Ближайший меньший элемент: {rI}, его индекс: {index}
Ближайший больший элемент: {array[max_index]} его индекс: {max_index}''')
    elif min_index < 0:
        print(f'''Ближайший больший элемент: {rI}, его индекс: {array.index(rI)}
В списке нет меньшего элемента''')
    elif rI > num:
        print(f'''Ближайший больший элемент: {rI}, его индекс: {array.index(rI)}
Ближайший меньший элемент: {array[min_index]} его индекс: {min_index}''')
    elif array.index(rI) == 0:
        print(f'Индекс введенного элемента: {array.index(rI)}')
else:
    print(f'Индекс введенного элемента: {binary_search(array, num, 0, len(array))}')
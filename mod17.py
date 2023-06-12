# def find(array, element):
#     for i, a in enumerate(array):
#         if a == element:
#             return i
#     return False
#
# array = list(map(int, input().split()))
# element = int(input())
#
# print(find(array, element))
# def binary_search(array, element, left, right):
#     if left > right:  # если левая граница превысила правую,
#         return False  # значит элемент отсутствует
#
#     middle = (right + left) // 2  # находимо середину
#     if array[middle] == element:  # если элемент в середине,
#         return middle  # возвращаем этот индекс
#     elif element < array[middle]:  # если элемент меньше элемента в середине
#         # рекурсивно ищем в левой половине
#         return binary_search(array, element, left, middle - 1)
#     else:  # иначе в правой
#         return binary_search(array, element, middle + 1, right)
# element = int(input())
# array = [i for i in range(1,100)] # 1,2,3,4,...
#
# # запускаем алгоритм на левой и правой границе
# print(binary_search(array, element, 0, 99))

#НАИВНАЯ СОРТИРОВКА
# import random  # модуль, с помощью которого перемешиваем массив
#
# # пусть имеем массив всего лишь из 9 элементов
# array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
#
# is_sort = False  # станет True, если отсортирован
# count = 0  # счетчик количества перестановок
#
# while not is_sort:  # пока не отсортирован
#     count += 1  # прибавляем 1 к счётчику
#
#     random.shuffle(array)  # перемешиваем массив
#
#     # проверяем, отсортирован ли
#     is_sort = True
#     for i in range(len(array) - 1):
#         if array[i] > array[i + 1]:
#             is_sort = False
#             break
#
# print(array)
# # [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(count)
# # 290698

#СОРТИРОВКА ВЫБОРОМ
# array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
# count = 0
# for i in range(len(array)):  # проходим по всему массиву
#     idx_min = i  # сохраняем индекс предположительно минимального элемента
#     for j in range(i, len(array)):
#         count += 1
#         if array[j] < array[idx_min]:
#             idx_min = j
#     if i != idx_min:  # если индекс не совпадает с минимальным, меняем
#         array[i], array[idx_min] = array[idx_min], array[i]
#
# print(array)
# print(count)

#СОРТИРОВКА ПУЗЫРЬКОМ
# array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
#
# for i in range(len(array)):
#     for j in range(len(array) - i - 1):
#         if array[j] > array[j + 1]:
#             array[j], array[j + 1] = array[j + 1], array[j]
#
# print(array)

#СОРТИРОВКА ВСТАВКАМИ
# array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
# count = 0
# for i in range(1, len(array)):
#     x = array[i]
#     idx = i
#     while idx > 0 and array[idx-1] > x:
#         count += 1
#         array[idx] = array[idx-1]
#         idx -= 1
#     array[idx] = x
# print (array)
# print(count)

#СОРТИРОВКА СЛИЯНИЕМ
# def merge_sort(L):  # "разделяй"
#     if len(L) < 2:  # если кусок массива меньше 2,
#         return L[:]  # выходим из рекурсии
#     else:
#         middle = len(L) // 2  # ищем середину
#         left = merge_sort(L[:middle])  # рекурсивно делим левую часть
#         right = merge_sort(L[middle:])  # и правую
#         return merge(left, right)  # выполняем слияние
#
#
# def merge(left, right):  # "властвуй"
#     result = []  # результирующий массив
#     i, j = 0, 0  # указатели на элементы
#
#     # пока указатели не вышли за границы
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#
#     # добавляем хвосты
#     while i < len(left):
#         result.append(left[i])
#         i += 1
#
#     while j < len(right):
#         result.append(right[j])
#         j += 1
#
#     return result

#Быстрая СОРТИРОВКА
array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
# def qsort(array, left, right):
#     middle = (left + right) // 2
#
#     p = array[middle]
#     i, j = left, right
#     while i <= j:
#         while array[i] < p:
#             i += 1
#         while array[j] > p:
#             j -= 1
#         if i <= j:
#             array[i], array[j] = array[j], array[i]
#             i += 1
#             j -= 1
#
#     if j > left:
#         qsort(array, left, j)
#     if right > i:
#         qsort(array, i, right)
# print(array)

def qsort_random(array, left, right):
    p = random.choice(array[left:right + 1])
    i, j = left, right
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:
            count += 1
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    if j > left:
        qsort_random(array, left, j)
    if right > i:
        qsort_random(array, i, right)
print(qsort_random(array, 0, len(array) -1))
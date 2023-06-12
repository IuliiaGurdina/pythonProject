# def par_checker(string):
#     stack = []  # инициализируем стек
#
#     for s in string:  # читаем строку посимвольно
#         if s == "(":  # если открывающая скобка,
#             stack.append(s)  # добавляем её в стек
#         elif s == ")":
#             # если встретилась закрывающая скобка, то проверяем
#             # пуст ли стек и является ли верхний элемент — открывающей скобкой
#             if len(stack) > 0 and stack[-1] == "(":
#                 stack.pop()  # удаляем из стека
#             else:  # иначе завершаем функцию с False
#                 return False
#     # если стек пустой, то незакрытых скобок не осталось
#     # значит, возвращаем True, иначе — False
#     return len(stack) == 0
# print(par_checker("(5+6)*(7+8)/(4+3)"))
#
# pars = {")": "(", "]": "["}
#
#
# def par_checker_mod(string):
#     stack = []
#
#     for s in string:
#         if s in "([":
#             stack.append(s)
#         elif s in ")]":
#             if len(stack) > 0 and stack[-1] == pars[s]:
#                 stack.pop()
#             else:
#                 return False
#     return len(stack) == 0
#
# N_max = int(input("Определите размер очереди:"))
#
# queue = [0 for _ in range(N_max)]  # инициализируем список с нулевыми элементами
# order = 0  # будем хранить сквозной номер задачи
# head = 0  # указатель на начало очереди
# tail = 0  # указатель на элемент следующий за концом очереди
#
# while True:
#     cmd = input("Введите команду:")
#     if cmd == "empty":
#         if is_empty():
#             print("Очередь пустая")
#         else:
#             print("В очереди есть задачи")
#     elif cmd == "size":
#         print("Количество задач в очереди:", size())
#     elif cmd == "add":
#         if size() != N_max:
#             add()
#         else:
#             print("Очередь переполнена")
#     elif cmd == "show":
#         if is_empty():
#             print("Очередь пустая")
#         else:
#             show()
#     elif cmd == "do":
#         if is_empty():
#             print("Очередь пустая")
#         else:
#             do()
#     elif cmd == "exit":
#         for _ in range(size()):
#             do()
#         print("Очередь пустая. Завершение работы")
#         break
#     else:
#         print("Введена неверная команда")
#
#
# def is_empty(): # очередь пуста?
#     # да, если указатели совпадают и в них содержится ноль
#     return head == tail and queue[head] == 0
# def size(): # получаем размер очереди
#     if is_empty(): # если она пуста
#         return 0 # возвращаем ноль
#     elif head == tail: # иначе, если очередь не пуста, но указатели совпадают
#         return N_max # значит очередь заполнена
#     elif head > tail: # если хвост очереди сместился в начало списка
#         return N_max - head + tail
#     else: # или если хвост стоит правее начала
#         return tail - head
#
#
# def add():  # добавляем задачу в очередь
#     global tail, order
#     order += 1  # увеличиваем порядковый номер задачи
#     queue[tail] = order  # добавляем его в очередь
#     print("Задача №%d добавлена" % (queue[tail]))
#
#     # увеличиваем указатель на 1 по модулю максимального числа элементов
#     # для зацикливания очереди в списке
#     tail = (tail + 1) % N_max
# def show(): # выводим приоритетную задачу
#     print("Задача №%d в приоритете" % (queue[head]))
# def do(): # выполняем приоритетную задачу
#     global head
#     print("Задача №%d выполнена" % (queue[head]))
#     queue[head] = 0 # после выполнения зануляем элемент по указателю
#     head = (head + 1) % N_max # и циклично перемещаем указатель

# G = {"Адмиралтейская" :
#          {"Садовая" : 4},
#      "Садовая" :
#          {"Сенная площадь" : 3,
#           "Спасская" : 3,
#           "Адмиралтейская" : 4,
#           "Звенигородская" : 5},
#      "Сенная площадь" :
#          {"Садовая" : 3,
#           "Спасская" : 3},
#      "Спасская" :
#          {"Садовая" : 3,
#           "Сенная площадь" : 3,
#           "Достоевская" : 4},
#      "Звенигородская" :
#          {"Пушкинская" : 3,
#           "Садовая" : 5},
#      "Пушкинская" :
#          {"Звенигородская" : 3,
#           "Владимирская" : 4},
#      "Владимирская" :
#          {"Достоевская" : 3,
#           "Пушкинская" : 4},
#      "Достоевская" :
#          {"Владимирская" : 3,
#           "Спасская" : 4}}
# D = {k : 100 for k in G.keys()} # расстояния
# start_k = 'Адмиралтейская' # стартовая вершина
# D[start_k] = 0 # расстояние от нее до самой себя равно нулю
# U = {k : False for k in G.keys()} # флаги просмотра вершин
# P = {k : None for k in G.keys()} # предки
#
# for _ in range(len(D)):
#     # выбираем среди непросмотренных наименьшее по расстоянию
#     min_k = min([k for k in U.keys() if not U[k]], key = lambda x: D[x])
#
#     for v in G[min_k].keys(): # проходимся по всем смежным вершинам
#          if D[v] > D[min_k] + G[min_k][v]: # если расстояние от текущей вершины меньше
#             D[v] = D[min_k] + G[min_k][v] # то фиксируем его
#             P[v] = min_k # и записываем как предок
#     U[min_k] = True # просмотренную вершину помечаем
# pointer = "Владимирская" # куда должны прийти
# while pointer is not None: # перемещаемся, пока не придём в стартовую точку
#     print(pointer)
#     pointer = P[pointer]
#
# class BinaryTree:
#     def __init__(self, value):
#         self.value = value
#         self.left_child = None
#         self.right_child = None
#     def insert_left(self, next_value):
#        if self.left_child is None:
#         self.left_child = BinaryTree(next_value)
#        else:
#         new_child = BinaryTree(next_value)
#         new_child.left_child = self.left_child
#         self.left_child = new_child
#        return self
#
#     def insert_right(self, next_value):
#         if self.right_child is None:
#             self.right_child = BinaryTree(next_value)
#         else:
#             new_child = BinaryTree(next_value)
#             new_child.right_child = self.right_child
#             self.right_child = new_child
#         return self
#
#     def pre_order(self):
#         print(self.value)  # процедура обработки
#
#         if self.left_child is not None:  # если левый потомок существует
#             self.left_child.pre_order()  # рекурсивно вызываем функцию
#
#         if self.right_child is not None:  # если правый потомок существует
#             self.right_child.pre_order()  # рекурсивно вызываем функцию
#
#     def post_order(self):
#         if self.left_child is not None:  # если левый потомок существует
#             self.left_child.post_order()  # рекурсивно вызываем функцию
#
#         if self.right_child is not None:  # если правый потомок существует
#             self.right_child.post_order()  # рекурсивно вызываем функцию
#
#         print(self.value)  # процедура обработки
#
#     def in_order(self):
#         if self.left_child is not None:  # если левый потомок существует
#             self.left_child.in_order()  # рекурсивно вызываем функцию
#
#         print(self.value)  # процедура обработки
#
#         if self.right_child is not None:  # если правый потомок существует
#             self.right_child.in_order()  # рекурсивно вызываем функцию
# # создаём корень и его потомков /7|2|5\
# node_root = BinaryTree(2).insert_left(7).insert_right(5)
# # левое поддерево корня /2|7|6\
# node_7 = node_root.left_child.insert_left(2).insert_right(6)
# # правое поддерево предыдущего узла /5|6|11\
# node_6 = node_7.right_child.insert_left(5).insert_right(11)
# # правое поддерево корня /|5|9\
# node_5 = node_root.right_child.insert_right(9)
# # левое поддерево предыдущего узла корня /4|9|\
# node_9 = node_5.right_child.insert_left(4)
# # node_root.post_order()
# node_root.in_order()

# class Node:  # класс элемента
#     def __init__(self, value=None, next_=None):  # инициализируем
#         self.value = value  # значением
#         self.next = next_  # и ссылкой на следующий элемент
#
#     def __str__(self):
#         return "Node value = " + str(self.value)
#
#
# class LinkedList:  # класс списка
#     def __init__(self):  # инициализируем пустым
#         self.first = None
#         self.last = None
#
#     def clear(self):  # очищаем список
#         self.__init__()
#
#     def __str__(self):  # функция печати
#         R = ''
#
#         pointer = self.first  # берем первый указатель
#         while pointer is not None:  # пока указатель не станет None
#             R += str(pointer.value)  # добавляем значение в строку
#             pointer = pointer.next  # идем дальше по указателю
#             if pointer is not None:  # если он существует добавляем пробел
#                 R += ' '
#         return R
#
#     def pushleft(self, value):
#         if self.first is None:
#             self.first = Node(value)
#             self.last = self.first
#         else:
#             new_node = Node(value, self.first)
#             self.first = new_node
#
#     def pushright(self, value):
#         if self.first is None:
#             self.first = Node(value)
#             self.last = self.first
#         else:
#             new_node = Node(value)
#             self.last.next = new_node
#             self.last = new_node
#
#     def popleft(self):
#         if self.first is None:  # если список пустой, возвращаем None
#             return None
#         elif self.first == self.last:  # если список содержит только один элемент
#             node = self.first  # сохраняем его
#             self.__init__()  # очищаем
#             return node  # и возвращаем сохраненный элемент
#         else:
#             node = self.first  # сохраняем первый элемент
#             self.first = self.first.next  # меняем указатель на первый элемент
#             return node  # возвращаем сохраненный
#
#     def popright(self):
#         if self.first is None:  # если список пустой, возвращаем None
#             return None
#         elif self.first == self.last:  # если список содержит только один элемент
#             node = self.first  # сохраняем его
#             self.__init__()  # очищаем
#             return node  # и возвращаем сохраненный элемент
#         else:
#             node = self.last  # сохраняем последний
#             pointer = self.first  # создаем указатель
#             while pointer.next is not node:  # пока не найдем предпоследний
#                 pointer = pointer.next
#             pointer.next = None  # обнуляем указатели, чтобы
#             self.last = pointer  # предпоследний стал последним
#             return node  # возвращаем сохраненный
#
#     def __iter__(self):  # объявляем класс как итератор
#         self.current = self.first  # в текущий элемент помещаем первый
#         return self  # возвращаем итератор
#
#     def __next__(self):  # метод перехода
#         if self.current is None:  # если текущий стал последним
#             raise StopIteration  # вызываем исключение
#         else:
#             node = self.current  # сохраняем текущий элемент
#             self.current = self.current.next  # совершаем переход
#             return node  # и возвращаем сохраненный
#
#     def __len__(self):
#         count = 0
#         pointer = self.first
#         while pointer is not None:
#             count += 1
#             pointer = pointer.next
#         return count
# LL = LinkedList()
#
# LL.pushright(1)
# LL.pushleft(2)
# LL.pushright(3)
# LL.popright()
# LL.pushleft(4)
# LL.pushright(5)
# LL.popleft()
#
# print(LL)
# print(len(LL))

#
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
# def count(array, element):
#     count = 0
#     for a in array:
#        if a == element:
#             count += 1
#     return count




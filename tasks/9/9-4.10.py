# Напишите функцию task_manager, которая принимает список задач для нескольких серверов. 

# Каждый элемент списка состоит из кортежа (<номер задачи>, <название сервера>, <высокий приоритет задачи>).

# Функция должна создавать словарь и заполнять его задачами по следующему принципу: название сервера — ключ, по которому хранится очередь задач для конкретного сервера. Если поступает задача без высокого приоритета (последний элемент кортежа — False), добавить номер задачи в конец очереди. Если приоритет высокий, добавить номер в начало.

# Для словаря используйте defaultdict, для очереди — deque.

# Функция возвращает полученный словарь с задачами.
from collections import defaultdict
from collections import deque
tasks = [(36871, 'office', False),
(40690, 'office', False),
(35364, 'voltage', False),
(41667, 'voltage', True),
(33850, 'office', False)]



def task_manager(tasks):
    serv  = defaultdict(deque)
    for task in tasks:
        if task[-1]:
            serv[task[1]].appendleft(task[0])
        else:
            serv[task[1]].append(task[0])
    return serv
print(task_manager(tasks))
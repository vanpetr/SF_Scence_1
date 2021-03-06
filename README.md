# Проект 0. Угадай число

## Оглавление  
[1. Описание проекта](.README.md#Описание-проекта)  
[2. Какой кейс решаем?](.README.md#Какой-кейс-решаем)  
[3. Краткая информация о данных](.README.md#Краткая-информация-о-данных)  
[4. Этапы работы над проектом](.README.md#Этапы-работы-над-проектом)  
[5. Результат](.README.md#Результат)    
[6. Выводы](.README.md#Выводы) 

### Описание проекта    
Угадать загаданное компьютером число за минимальное число попыток.

:arrow_up:[к оглавлению](_)


### Какой кейс решаем?    
Нужно написать программу, которая угадывает число за минимальное число попыток - не более 20 попыток.

**Условия соревнования:**  
- Компьютер загадывает целое число от 0 до 100, и нам его нужно угадать. Под «угадать», подразумевается «написать программу, которая угадывает число».
- Алгоритм учитывает информацию о том, больше ли случайное число или меньше нужного нам.

**Метрика качества**     
Результаты оцениваются по среднему количеству попыток при 1000 повторений

**Что практикуем**     
Учимся писать хороший код на python


### Краткая информация о данных
В алгоритме поиска:

В качестве входного параметра используется целочисленная переменная number (искомое случайное число).
Возвращается целочисленная переменная count (число попыток).

В алгоритме проверки качества:

В качестве входного параметра используется имя функции алгоритма поиска score_game.
В ходе выполнения алгоритма проверки качества формируется массив random_array из 1000 случайных целых чисел в интервале (1,100).
Возвращается значение score (среднее значение количества попыток, затраченных алгоритмом поиска до нахождения случайного числа).
  
:arrow_up:[к оглавлению](.README.md#Оглавление)


### Этапы работы над проектом  
В качестве алгоритма поиска выбран метод дихотомии
Проведена проверка качества работы алгоритма на выборке из 1000 случайных чисел. Среднее количество попыток - 5.

:arrow_up:[к оглавлению](.README.md#Оглавление)


### Результаты:  
По результатам проверки качества работы алгоритма среднее количество попыток - 5, что соответствует поставленной задаче.

:arrow_up:[к оглавлению](.README.md#Оглавление)


### Выводы:  
Метод дихотомии является одним из самых простых в  понимании и написании из эффективных методов оптимизации. 

:arrow_up:[к оглавлению](.README.md#Оглавление)

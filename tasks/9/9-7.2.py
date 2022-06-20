import numpy as np
arr = np.arange(8) # создать 1 d  массив
print(arr)
arr.shape = (2, 4) # поменять форму массива на 2 d 
print(arr)
arr1 = np.arange(8)
arr_new = arr1.reshape((2, 4)) # создать измененный клон массива
print(arr1)
print(arr_new)
arr_new1 = arr1.reshape((2, 4), order="F") # заполнение по столбцам, по умолчанию order = "C"
print(arr_new1)
arr_trans = arr_new.transpose() # меняет строки и столбцы местами
print(arr_trans)
arr = np.linspace(1, 2, 6)
print(arr[2])
print(arr[::-1])
nd_array =  np.linspace(0, 6, 12, endpoint=False).reshape(3,4)
print(nd_array)
print(nd_array[1:, 2:4]) # срез всех строк со второй по столбцам с 3го по 4й
print(nd_array[:, 2:4]) # всех строк по столбцам 3 и 4
print(nd_array[:2]) # срез всех строк до 3й строки целиком
print(nd_array)
print(nd_array[::-1, -1])
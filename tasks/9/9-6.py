import numpy as np
arr = np.array([1,5,2,9,10])
arr
# array([ 1,  5,  2,  9, 10])
print(type(arr))

nd_arr = np.array([
               [12, 45, 78],
               [34, 56, 13],
               [12, 98, 76]
               ])
print(type(nd_arr))

print(arr.dtype)
arr = np.array([1,5,2,9,10], dtype=np.int8)
print(arr.dtype) # тип данных
print(arr.ndim)
print(nd_arr.ndim) # размерность
print(arr.size) # размер
print(arr.shape) # структура
print(arr.itemsize) # размер в байтах
zeros_1d = np.zeros(5)# создать массив с 5ю нулевыми ячейками
print(zeros_1d)
zeros_3d = np.zeros((5,4,3), dtype=np.float32) # создать пустой 3d массив с плавующей точкой точности 32
print(zeros_3d.shape)
print(np.arange(5))
print(np.arange(2.5, 5))
print(np.arange(2.5, 5, 0.5, dtype=np.float16)) # создание массивов генератором чисел
print(np.linspace(1, 2, 10)) # создание массива с плавующей точкой
print(np.linspace(1, 2, 10, endpoint=False))
print(np.linspace(1, 2, 10, endpoint=True, retstep=True)) # arr, step = 
print(np.linspace(1, 2, 10, endpoint=False, retstep=True))
arr, step = np.linspace(1, 2, 10, endpoint=True, retstep=True)
print(step) # шаг между числами
arr1, step1 = np.linspace(-6, 21, 60, endpoint=False, retstep=True)
print(round(step1,2))
import numpy as np
import pandas as pd

# Объект 'Series' представляет собой аналог одномерного массива
data = ['Петя', 'Олег', 'Вася']
s = pd.Series(data)
print(s)
# Данные могут быть разных типов
s = pd.Series(['Ольга', 1, 3.4, np.nan])
print(s)
# Модуль сам определяет тип даынных
s = pd.Series([1, 3.4, 2.3])
print(s)
# Можно задавать индексы
s = pd.Series([1, 3.4, 2.3, 5], index=['a', 'b', 'c', 'd'])
print(s)
print(s.ndim) # для Series ответ всегда 1
print(s.shape) # для Series ответ всегда (количество_элементов,)
print(s.dtype) # возвращает тип данныз
print(s.size) # возвращает количество данных

#Можно преобразовать в массив numpy
nps = s.to_numpy()
print(nps)

# Индексы и выборка
s = pd.Series(np.random.randn(8), index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
print(s, '\n')
print(s[2:4], '\n') # отбираем элементы с 2го по 4й (не включительно)
print(s[(s > 0) & (s < 1)], '\n') # отбираем элементы 0 < s < 1
print(s[['b', 'g', 'h']]) # доступ по метке

# Добавление и удаление элементов
s['nnn'] = 34
print(s)
s.drop(labels=['a', 'nnn'])
print(s)

"""ОПЕРАЦИИ"""
print("s + s")
print(s + s)
print("s * s")
print(s * s)
print("s ** 2")
print(s ** 2)
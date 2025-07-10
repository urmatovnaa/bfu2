import numpy as np
import pandas as pd

# DATAFRAME
df = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(df)

df = pd.DataFrame({'first': [1, 2, 3], 'second': [4, 5, 6], 'third': [7, 8, 9]})
# print(df)

df.describe() # Сводная информация для числовых колонок
# print(df.describe())
# генерация
# print(df.value_counts())

"""Доступ к строкам возмоден несколькими способами:
loc используется для доступа по строковой метке (индексу)
iloc используется для доступа по числовому индексу"""

df = pd.DataFrame({'first': [1, 2, 3, 5, 6, 7, 3], 'second': [4, 5, 6, 6, 45, 23, 34], 'third': [7, 8, 9, 10, 11, 12, 14]}, index=['f', 'd', 'f', 's', 'z', 'a', 'w'])
print(df)
# print(df.loc['f'])
# print(df.iloc[[0], [2]])
# df.head()
print('mean age =', df['first'].mean())
print('max age =', df['first'].max())

# Группировка и сортировка
print(df.sort_values('first', ascending=False).head())

print(df.groupby(['first'])['second'].aggregate(np.mean))


## Памятка
### numpy - крутая работа с массивами
```py
import numpy as np

np_list = np.array([1,2,3,45,6, 'f']) # все элементы одного типа
```
### Pandas - начало работы с pandas 

```py
import pandas as pd
```

#### Создание Series

```py
data = pd.Series( [1,2,3,4,5], index=['A', 'B', 'C', 'D', 'E'], name='Sheat')
```

#### lesson 1 - создание датафрейма

```py
data = {
    "fedya": [21, 'Yoshakar-Ola', 'Volgastate University'],
    "petya": [25, 'Yoshakar-Ola', 'Gubkino']
}

df = pd.DataFrame(data, index=['age', 'city', 'univercity'])
```

### Practice чуток NumPy

##### Создать 5 на 5 массив с 1 до 24
```py
array_5x5 = np.range(25).reshape(5,5)
```

###### то есть .reshape() может помочь преобразовать формат массива 

##### Сумму элементов в массиве new_array = array_5x5.reshape(1,25) с помощью sum
sum - встроенный метод np
```py
new_array = array_5x5.reshape(1,25)

array_sum = np.sum(array_5x5)
```
##### Вывести 1 элемент в каждом подмассиве array_5x5 а затем и все элементы второго подмассива 
```py
print(array_5x5[:,0])
print(array_5x5[2,:])
```
##### Вывести элементы > 10
```py
list_5x5[list_5x5>10]
```

### Practice чуток Pandas 

##### Вывести элементы которые больше какого то значения (5) из серис

```py
ser[ser>5]
```

##### Создать Series от 0 до 9 вкл где индексы будут в обратном порядке идти

```py
ser1 = pd.Series(range(10), index = range(10,0,-1))
```

##### Эквивалент map - метод apply (применяет функцию к итерируемому обьекту(к элементам))

```py
def add_two(elem: int) -> int:
    return elem+2

ser_new = ser1.apply(add_two)
```

#### Генерация и использование тестовых данных с помощью сервиса Mockaroo и формата CSV

##### Генерировать данные можно через https://www.mockaroo.com/

```py
telegram_accounts=pd.read_csv("MOCK_DATA.csv")
```
##### Показывать много строк в окне 
```py
pd.set_option("display.min_rows", 1000)
telegram_accounts
pd.reset_option("display.min_rows")
```
![тут пример](img/set_option_displaymin_rows.png)

#### Инструменты loc, iloc.

##### Для начала поймем, что в

```py
data = {
    "fedya": [21, 'Yoshakar-Ola', 'Volgastate University'],
    "petya": [25, 'Yoshakar-Ola', 'Gubkino']
}
```
* fedya и petya - названия столбцов, строки определяются индексами:

```py
df = pd.DataFrame(data, index=['age', 'city', 'univercity'])
```

##### КЛЮЧИ СЛОВАРЯ - ЭТО НАЗВАНИЯ СТОЛБЦОВ, ЕСЛИ НЕ ЗАДАТЬ ИНДЕКСЫ ТО БУДЕТ СЛЕДУЮЩАЯ КАРТИНА:

![тут пример](img/without_index.png)

##### Но надо обращать внимание на исходник, типо если словарь будет:
```py
data_2 = {
    'name': ['fedya', 'petya', 'kamilla', 'tanya'],
    'age': [21, 25, 20, 25],
    'city': ['New York', 'Moscow', 'Kazan', 'Vashington']
}
```
##### Бурмалда выглядит так:

![тут пример](img/колонки-наоборот.png)

##### Короче пока нихуя не понятно, как делать надо, я так сказал для понимания.

```py
df.iloc[0:2]
df.iloc[3:]
df.iloc[:, 0] #Выбирает все строки, но только первый столбец
df.iloc[:, [0,1]] #Выбирает все строки и первые два столбца по позициям
```

##### Фильтрация

```py
df.loc[df['age'] > 18]

df.loc[df['age']> 18, ['name', 'adress']]

df.loc[(df['age']> 18) &  (df['gender'] == 'female'), ['name', 'adress']]

#Можно и без loc

df[df['age']>18] # но здесь нельзя указать столбцы как при loc - плохой тон короче(небезопасно, непредпочтительно)
```

###### Для сложных условий можно использовать:

```py
df.query(" age>30 and city == 'Moscow' ") # колокни без кавычек
```
Вот код попрактиковаться:
```py

df_new = pd.DataFrame({
    'name': ['Anna', 'Bob', 'Charlie', 'Diana'],
    'age': [25, 35, 28, 42],
    'city': ['Moscow', 'SPb', 'Moscow', 'Kazan'],
    'salary': [50000, 75000, 60000, 90000]
}, index=['a', 'b', 'c', 'd'])

df_new.loc[(df_new['age']<30) & (df_new['city'] == 'Moscow')]

df_new.query(" age < 30 and city == 'Moscow' ")

df_new.loc[df_new['age']>40, ['salary']] *= 1.2
```

##### Задать индекс: 
```py
df.set_index('column', inplace = True/False)
```

#### Принудительное преобразование типов 
```py
df['id_movie'] = df['id_movie'].astype('str') 
```

#### Работа с датами

```py
# Преобразование строки → datetime
df['birthday'] = pd.to_datetime(df['birthday'], format='%d.%m.%Y')

# Извлечение компонентов
df['birthday'].dt.year   # месяц, день, hour, minute, second

# Округление времени
df['birthday'].dt.round('D')   # до дней
df['birthday'].dt.floor('H')   # вниз до часов
df['birthday'].dt.ceil('T')    # вверх до минут

# Округление до месяца
df['birthday'].dt.to_period('M').dt.to_timestamp()

# Арифметика с датами (возраст в секундах)
diff = pd.to_datetime('01.09.2023', format='%d.%m.%Y') - df['birthday']
diff.dt.total_seconds()
```

#### Пропущенные значения

```py
# Подсчёт пропусков
df['grade'].isna().sum()

# Замена на среднее (без учёта NaN)
mean_val = df['grade'].dropna().mean().round()
df['grade'] = df['grade'].fillna(mean_val).astype('int')
```
#### Строковые методы
```py
df['gender'] = (df['gender']
                .str.replace('М', 'Мужской', regex=False)
                .str.replace('Ж', 'Женский', regex=False))

# Доступны: .str.lower(), .str.upper(), .str.contains(), .str.strip() и др.
```
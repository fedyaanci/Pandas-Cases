# Инспекция данных

### Разведка

```py
df.head(5) / df.tail(5)       # первые/последние строки
df.shape                      # (строки, колонки)
df.info()                     # типы, память, кол-во не-NA
df.describe()                 # статистика по числам (count, mean, std, квинтили)
df.dtypes                     # типы колонок
df.nunique()                  # кол-во уникальных значений по колонкам
df.unique()                   # series из уникальных значений 
df.isna().sum()               # кол-во пропусков
len(df)                       # длина обьекта, можно и к series
df.columns                    # список колоночек
df.size                       # всего ячеек (строки × колонки)
df['column'].value_counts()   # сколько раз встречается каждое значение
df.isna().mean()              # Доля пропусков (0.05 = 5% пропусков)
df.notna()                    # Используется в фильтрации df[df['age'].notna()]
```

### Очистка данных

```py
# удалить строки с любым пропуском
df.dropna()

# удалить строки, где пропуск в конкретной колонке
df.dropna(subset=['name'])

# удалить колонки, где есть хоть один пропуск
df.dropna(axis=1)

# заполнить пропуски константой
df['salary'].fillna(0)

# заполнить пропуски средним/медианой
df['age'].fillna(df['age'].mean())
df['age'].fillna(df['age'].median())

# интерполяция (линейная между значениями)
df['age'].interpolate()
```

### Удаление дупликатов

```py 
# удалить полностью одинаковые строки
df.drop_duplicates()

# удалить дубли по конкретной колонке (оставить первое)
df.drop_duplicates(subset=['name'], keep='first')

# удалить дубли, оставив последнее
df.drop_duplicates(subset=['id'], keep='last')
```

### Приведение типов

```py
# приведение типа 
df['age'] = pd.to_datetime(user['birthday'], format='%d.%m.%Y')

# строка - число (ошибки - nan)
df['age'] = pd.to_numeric(df['age'], errors='coerce')

# число - строка
df['id'] = df['id'].astype(str)

# строка - дата
df['date'] = pd.to_datetime(df['date'], errors='coerce')

Хоро
```

### Очистка строк

```py

df.drop(columns=['grade'])

# убрать пробелы по краям
df['name'] = df['name'].str.strip()

# привести к нижнему/верхнему регистру
df['name'] = df['name'].str.lower() # str - окуляр
df['name'] = df['name'].str.upper()

# заменить подстроку
df['city'] = df['city'].str.replace('МСК', 'Москва')
```

### Замена значений

```py
# заменить одно значение на другое
df['city'] = df['city'].replace('МСК', 'Москва')

# заменить несколько значений (словарь)
df['city'] = df['city'].replace({'МСК': 'Москва', 'СПБ': 'Петербург'})

# хорошая практика замены значений на средее
mean_grade = user['grade'].dropna().mean().round()
user['grade'] = user['grade'].fillna(mean_grade).astype('int')

# заменить по условию
df.loc[df['age'] > 100, 'age'] = np.nan  # возраст >100 - пропуск
df.loc[df['salary'] < 0, 'salary'] = 0   # отрицательная зп - 0

# заменить через map (для категориальных)
mapping = {'МСК': 1, 'СПБ': 2, 'КЗН': 3}
df['city_code'] = df['city'].map(mapping)  # не найденные → nan
```

### Антипаттерн

```py
for tup in df.itertuples():  
    print(tup.gender)
```
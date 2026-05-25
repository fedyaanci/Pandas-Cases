# Группировка 

### Пример(тесовый датафрейм)
```py
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'dept': ['IT', 'IT', 'HR', 'HR', 'Sales', 'Sales'],
    'city': ['МСК', 'СПБ', 'МСК', 'МСК', 'СПБ', 'СПБ'],
    'name': ['Анна', 'Борис', 'Виктор', 'Галина', 'Дмитрий', 'Елена'],
    'salary': [80000, 90000, 50000, 55000, 70000, 75000],
    'age': [25, 30, 28, 35, 40, 29]
})
```

### Базовая группировка + 1 агрегация
```py
# Средняя зарплата по отделам
df.groupby('dept')['salary'].mean()
```

### Цепочка агрегаций 
```py
# cумма, кол-во, среднее — цепочкой
df.groupby('dept')['salary'].agg(['sum', 'count', 'mean'])

        sum  count     mean
dept                       
HR    105000      2  52500.0
IT    170000      2  85000.0
Sales 145000      2  72500.0
```

### Цепочка агрегаций для разных колонок

```py
df.groupby('dept)\
    .agg(
        'salary': ['min','max', 'mean']
        'age': 'min',
        'name': 'count'
    )
```

### Группировка по нескольким колонкам

```py
# зп по отделу + городу
df.groupby(['dept', 'city'])['salary'].mean()
```

### Агрегация с сохранением размера

```py
df['avg_calary_dept'] = df.groupby(['dept','salary']).transform('mean')
```

### Группировка + Фильтр + apply(lambda)
filter — оставить только группы, удовлетворяющие условию

```py
# оставить только отделы, где средняя ЗП > 60000
df.groupby('dept').filter(lambda x: x['salary'].mean() > 60000)

# Разница между макс и мин ЗП в отделе
df.groupby('dept')['salary'].apply(lambda x: x.max() - x.min())
```

### Подсказка
|Что сделать|Способ|
|:-:|:-:|
|Посчитать статистику по группе | groupby().agg()|
|Добавить групповую статистику к строкам | groupby().transform()|
|Отфильтровать целые группы | groupby().filter()|
|Сложная логика на группу |groupby().apply()|
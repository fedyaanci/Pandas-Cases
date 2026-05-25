# Объединение таблиц

### Соединить по общему значению - merge
```py
pd.merge(left_df, right_df, on='key_column', how='inner')
#how = {inner, left, right, outer}
```
Если разные имена колонок, по которым соединяем, то 
```py
pd.merge(t1, t2, left_on='id', right_on='user_id', suffixes=('_orders', '_users'))
# suffixes = ((_x, _y)) - если одна и та же колонка есть и в t1 и в t2
```
Контроль дублей:
```py
# ключ уникальный в обеих таблицах (1 к 1)
pd.merge(df1, df2, on='id', validate='1:1') 
# ключ уникальный слева, но может повторяться справа (1 ко многим)
pd.merge(df1, df2, on='id', validate='1:m') 
```

### Склеивание таблиц одинаковой структуры или просто добавление инф-ции
###### Аналог UNION ALL в SQL
Используется, когда таблицы одинаковой структуры (те же колонки) или нужно просто прилепить одно к другому. Здесь нет поиска совпадений по ключу.


```py
# Вертикально
df_new = pd.concat([df_part1, df_part2], ignore_index=True) #ignore_index=True - сбрасывает старый индекс

#Горизонтально
df_wide = pd.concat([df_stats, df_prices], axis=1) # соединяет по индексу, дырки - nan
```

### Быстрое соединение по индексу
df.join() 
* Всегда соединяет по индексу левой таблицы
* По умолчанию делает left join
  
```py
# делаем user_id индексом во второй таблице
users_indexed = users.set_index('user_id')

# соединяем
orders.join(users_indexed)
```



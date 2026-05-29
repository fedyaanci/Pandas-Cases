# pandasql 
#### — это Python-библиотека, которая позволяет выполнять SQL-запросы к pandas.DataFrame, не выходя из экосистемы pandas.

Под капотом sqlite:

* Берёт переменные DataFrame из вашего окружения (globals() или locals())
* Создаёт временную таблицу в памяти SQLite
* Выполняет SQL-запрос
* Конвертирует результат обратно в pandas.DataFrame

паттерн:
```py
pysql = lambda q: sqldf(q, globals())

res = pysql("""
    SELECT city, SUM(sales) as total_sales
    FROM df
    GROUP BY city
    HAVING total_sales > 200
    ORDER BY total_sales DESC
""")

print(res)
```
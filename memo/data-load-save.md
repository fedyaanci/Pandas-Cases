# Data-Loading csv.
```py
df = pd.read_csv('/path_to_file', sep=',', )

df = pd.read_csv('/path_to_file', sep=',', index_col='date') #задать индекс по 
df = pd.read_csv('/path_to_file', sep=',', index_col=0) # задать индекс по 1 колонке
df = pd.read_csv('/path_to_file', sep=',', index_col=[0, 1]) # мультииндекс

df = pd.read_csv('file.csv', header=2) # заголовок в 3-й строке

df = pd.read_csv('file.csv', parse_dates=['date', 'created_at']) #парсим колонки как тип date
df = pd.read_csv('file.csv', parse_dates=[['date', 'time']]) #  склеивает две колонки в одну новую с именем 'date_time' 
#и сразу парсит её как datetime. удобно, когда дата и время лежат в разных столбцах CSV.
df = pd.read_csv('file.csv', parse_dates=['date'], format='%d/%m/%Y') # формат даты (ускоряет парсинг)
df = pd.read_csv('file.csv', parse_dates=['date'], dayfirst=True) #dayfirst - flag(д м г)

df = pd.read_csv('file.csv', na_values=['NA', 'null', 'n/a']) # для грязного чтения
df = pd.read_csv('file.csv', dtype={'id': 'int32', 'name': 'category'})  # Типы данных (ускоряет + экономит память)


df = pd.read_csv('sales.csv', 
                 sep=';', 
                 index_col='order_id', 
                 parse_dates=['date'], 
                 na_values=['-', 'N/A'],
                 dtype={'customer_id': 'int32'})

            
for chunk in pd.read_csv('/file_to_path', chunksize=10000): # чтение по частям (большие файлы) читает по 1000 строк
    process(chunk)

df = pd.read_csv('https://example.com/data.csv') # URL
```
# Data-Saving csv.

```py
df.to_csv('out.csv', index=False)              # без индекса
df.to_csv('out.csv', sep=';', index=False)     # с разделителем
df.to_csv('out.csv', columns=['a', 'b'])       # только нужные колонки
df.to_csv('out.csv', date_format='%Y-%m-%d')   # формат дат
```

# Data-Loading excel.
```py
df = pd.read_excel('file.xlsx')

# указать лист
df = pd.read_excel('file.xlsx', sheet_name='Sheet2')     # по имени
df = pd.read_excel('file.xlsx', sheet_name=0)            # первый лист

# без заголовка
df = pd.read_excel('file.xlsx', header=None)

# чтение из старых .xls
df = pd.read_excel('file.xls', engine='xlrd')

# все листы сразу
sheets = pd.read_excel('file.xlsx', sheet_name=None)
df1 = sheets['Sheet1']
df2 = sheets['Sheet2']
```

# Data-saving xlsx
```py
df.to_excel('output.xlsx')

# без индекса
df.to_excel('output.xlsx', index=False)

# указать лист
df.to_excel('output.xlsx', sheet_name='MyData')

# без заголовка
df.to_excel('output.xlsx', header=False)
```
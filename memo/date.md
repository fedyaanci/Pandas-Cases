# Datetime

```py
df = pd.read_csv('data.csv', parse_dates=[['date', 'time']])

df['date'] = pd.to_datetime(df['date_str'], format='%Y-%m-%d')
df['date'] = pd.to_datetime(df['date_str'], format='%d.%m.%Y %H:%M')

df['date'] = pd.to_datetime(df['date_str'], errors='coerce')  # ошибки → NaT
df['date'] = pd.to_datetime(df['date_str'], errors='ignore')  # оставить как есть

```

## Извлечение компонентов

```py
df = pd.DataFrame({'date': pd.to_datetime(['2024-03-15 14:30:00', '2024-01-20 09:15:00'])})

# год, месяц, день
df['year'] = df['date'].dt.year        # 2024, 2024
df['month'] = df['date'].dt.month      # 3, 1
df['day'] = df['date'].dt.day          # 15, 20

# день недели (0=понедельник, 6=воскресенье)
df['weekday'] = df['date'].dt.weekday           # 4, 5
df['weekday_name'] = df['date'].dt.day_name()   # 'Friday', 'Saturday'

# квартал, неделя года
df['quarter'] = df['date'].dt.quarter    # 1, 1
df['week'] = df['date'].dt.isocalendar().week  # 11, 3

# время
df['hour'] = df['date'].dt.hour          # 14, 9
df['minute'] = df['date'].dt.minute      # 30, 15
```

### Разница между датами 
```py
# Разница двух дат
df['days_since'] = pd.Timestamp.today() - df['date']
df['days_since'].dt.days  # только дни (int)

# Прибавить/отнять время
df['next_week'] = df['date'] + pd.Timedelta(days=7)
df['prev_hour'] = df['date'] - pd.Timedelta(hours=1)

# Создать Timedelta
pd.Timedelta(days=5, hours=3, minutes=30)
```
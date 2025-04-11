import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Series with custom index cерия с кастомным индексом


s = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
print("\nCUSTOM INDEX SERIES:")
print(s)
"""
Задача 1: Создайте Series с температурами за неделю (пн-вс)  Create Series with weekly temperatures (Mon-Sun)
""""""сначала создаем два основных объекта в Pandas - Series  и DataFrame-  столбец и  таблица с названиями столбцов
"""

#temps = pd.Series([22, 23, 21, 20, 19, 22, 24], 
#                 index=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])

#=================DATAFRAME OPERATIONS===================
#Creating DataFrame from dict создание DataFrame из словаря
data = {
    'Product': ['Laptop', 'Phone', 'Tablet', 'Monitor'],
    'Price': [1200, 800, 400, 300],
    'Stock': [15, 30, 45, 20]
}
df = pd.DataFrame(data)
print("\nPRODUCT DATAFRAME:")
print(df)

"""
Задача 2: Добавьте столбец 'Total' (Price * Stock) ------- Add 'Total' column (Price * Stock)
"""
 

#df['Total'] = df['Price'] * df['Stock']

#multi-condition selection множественный выбор
#Выбираем товары по условиям
print("\nEXPENSIVE ITEMS IN STOCK:")
print(df[(df['Price'] > 500) & 
         (df['Stock'] < 20)])

"""
Задача 3: Выберите товары с ценой < 500 И запасом > 25  ------ Select items with price < 500 AND stock > 25
"""

#print(df[(df['Price'] < 500) & (df['Stock'] > 25)])

# Handling duplicates работа с дубликатами
df_with_dupes = pd.DataFrame({
    'City': ['Moscow', 'Berlin', 'Moscow', 'Paris'],
    'Visits': [10, 5, 10, 8]
})
print("\nDUPLICATES EXAMPLE:")
print(df_with_dupes.duplicated())

"""
Задача 4: Удалите дубликаты из df_with_dupes   ----Remove duplicates from df_with_dupes
"""
#print(df_with_dupes.drop_duplicates())



#Groupby with aggregation / Группировка с агрегацией
sales = pd.DataFrame({
    'Region': ['East', 'West', 'East', 'West'],
    'Sales': [250, 300, 200, 350]
})
print("\nGROUPBY EXAMPLE:")
#cчитаем статистику по группам как сводные таблицы   Aggregate data like pivot tables:

print(sales.groupby('Region').agg({'Sales': ['sum', 'mean']}))

"""
Задача 5: Добавьте столбец 'Month' и сгруппируйте по Region и Month Add 'Month' column and group by Region and Month
"""
#sales['Month'] = ['Jan', 'Jan', 'Feb', 'Feb']
#print(sales.groupby(['Region', 'Month']).sum())



#Working with dates                             работа с датами
date_rng = pd.date_range(start='1/1/2023', end='1/08/2023', freq='D')
ts_df = pd.DataFrame(date_rng, columns=['date'])
ts_df['value'] = np.random.randint(0,100,size=(len(date_rng)))
print("\nTIME SERIES EXAMPLE:")
print(ts_df.head())# Первые строки / First rows

"""
Задача 6: Отфильтруйте только первые 3 дня января
Filter only first 3 days of January
"""
#print(ts_df[ts_df['date'] <= '2023-01-03'])

#simple plotting простая визуализация

#df.plot(x='Product', y='Price', kind='bar', title='Product Prices')
#plt.show()

"""
Задача 7: Постройте круговую диаграмму по столбцу 'Stock'     -----------Plot pie chart for 'Stock' column
"""
#df.plot(y='Stock', kind='pie', labels=df['Product'])
#plt.show()

#web scraping example пример веб-скрапинга

# url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv'
# tips = pd.read_csv(url)
# print(tips.head())

"""
Задача 8: Посчитайте средний чек по дням недели
Calculate average bill by day of week
"""
#print(tips.groupby('day')['total_bill'].mean())




from datetime import datetime, timedelta

#working with Sales Data ###

sales = pd.DataFrame({  #sample sales data from an e-commerce store
    'order_id': [101, 102, 103, 104, 105],
    'product': ['Wireless Earbuds', 'Smart Watch', 'Phone Case', 'Tablet', 'Laptop'],
    'category': ['Electronics', 'Electronics', 'Accessories', 'Electronics', 'Electronics'],
    'price': [79.99, 199.99, 24.99, 349.99, 999.99],
    'quantity': [2, 1, 3, 1, 1],
    'order_date': pd.to_datetime(['2023-01-15', '2023-01-16', '2023-01-16', 
                                '2023-01-17', '2023-01-18'])
})

print("Sales Summary:")
print(f"Total orders: {len(sales)}")
print(f"Total revenue: ${sales['price'].sum():.2f}")
print(f"Average order value: ${sales['price'].mean():.2f}\n")

#add columns and 10% 
sales['revenue'] = sales['price'] * sales['quantity']
sales['discounted_price'] = sales['price'] * 0.9  #10% discount

print("Enhanced Sales Data:")
print(sales[['product', 'price', 'quantity', 'revenue']].head())


#generate 30 days of random temperature data
dates = pd.date_range(start='2023-06-01', periods=30)
temps = pd.DataFrame({
    'date': dates,
    'temperature': np.random.randint(65, 95, size=30),
    'humidity': np.random.randint(30, 90, size=30)
})

#calculate 7-day moving average
#Анализируем данные по дням/неделям:
temps['7_day_avg'] = temps['temperature'].rolling(window=7).mean()

hottest_days = temps.nlargest(3, 'temperature')
print("\nHottest Days:")
print(hottest_days[['date', 'temperature']])


#messy customer data
customers = pd.DataFrame({
    'cust_id': [1, 2, 3, 4, 5],
    'name': ['John Smith', 'Alice Johnson', 'Bob Brown', 'Mary Davis', ''],
    'email': ['john@example.com', 'alice@example', 'bob@example.com', 
             'mary.davis@example.com', np.nan],
    'signup_date': ['2023-01-15', '2023-02-28', '2023-03-10', 
                   '03/15/2023', '2023-04-01'],
    'purchases': ['$150', '200', '$175', '$300', '50']
})

customers_clean = customers.copy()
customers_clean['name'] = customers_clean['name'].str.strip().replace('', 'Unknown')
customers_clean['email'] = customers_clean['email'].where(
    customers_clean['email'].str.contains('@', na=False), np.nan)
customers_clean['signup_date'] = pd.to_datetime(
    customers_clean['signup_date'], errors='coerce')
customers_clean['purchases'] = customers_clean['purchases'].str.replace(
    '[^\d]', '', regex=True).astype(float)

print("\nCustomer Data Before Cleaning:")
print(customers.head())
print("\nAfter Cleaning:")
print(customers_clean.head())

#merging and aggregating Data

purchases = pd.DataFrame({
    'cust_id': [1, 2, 2, 3, 4, 6],
    'order_date': pd.to_datetime(['2023-01-20', '2023-03-05', '2023-03-15',
                                '2023-03-12', '2023-04-10', '2023-05-01']),
    'amount': [89.99, 120.50, 45.75, 230.00, 55.25, 199.99]
})

customer_activity = pd.merge(
    #merge customer data 
    customers_clean, purchases, on='cust_id', how='left')

#calculate
customer_stats = customer_activity.groupby('cust_id').agg({
    'name': 'first',
    'purchases': 'sum',
    'amount': 'sum'
}).rename(columns={'amount': 'total_spent'})

print("\nCustomer Spending Analysis:")
print(customer_stats)



print("\nData Inspection:")# always inspect data first
print(sales.info())# Типы данных / Data types
print(sales.describe())

sales['high_value'] = sales['revenue'] > 200  #vectorized operations instead of loops better than looping

#document data transformations
# Convert order_date to datetime (was already done during creation)
# sales['order_date'] = pd.to_datetime(sales['order_date'])

#save your processed data

sales.to_csv('processed_sales.csv', index=False)

print("\nAnalysis complete! Ready for more tasks.")
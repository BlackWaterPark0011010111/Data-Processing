import sqlite3
import csv
import logging

logging.debug("a debug message")
logging.info("an info")
logging.warning("a warning message")
logging.error("an error")
logging.criticaal("a message of critical severity")

# Параметры базы данных
db_name = "city_database.sqlite"

# Создаём соединение с SQLite
conn = sqlite3.connect(db_name)
cursor = conn.cursor()

# Создаём таблицу
create_table_query = """
CREATE TABLE IF NOT EXISTS city (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    city_name TEXT NOT NULL,
    country TEXT NOT NULL,
    population INTEGER,
    area_km2 REAL
);
"""
cursor.execute(create_table_query)
print("Таблица 'city' успешно создана.")

# Путь к файлу CSV
file_path = "City_List.csv"

# Загружаем данные из CSV в таблицу
with open(file_path, mode='r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Пропускаем заголовок
    for row in csv_reader:
        if len(row) < 4:  # Проверяем, что строка содержит все данные
            continue
        city_name = row[0].strip()
        country = row[1].strip()
        population = int(row[2].strip()) if row[2].strip().isdigit() else None
        area_km2 = float(row[3].strip()) if row[3].strip().replace('.', '', 1).isdigit() else None

        # Вставляем данные в таблицу
        cursor.execute(
            "INSERT INTO city (city_name, country, population, area_km2) VALUES (?, ?, ?, ?)",
            (city_name, country, population, area_km2)
        )

# Сохраняем изменения и закрываем соединение
conn.commit()
cursor.close()
conn.close()

print("Данные успешно загружены в таблицу 'city'.")

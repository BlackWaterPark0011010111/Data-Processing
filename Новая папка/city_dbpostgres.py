import psycopg2
import csv
 #                  chcp 65001
 #                 SET client_encoding = 'UTF8';
# Параметры подключения
conn = psycopg2.connect(
    dbname="city",
    user="postgres",
    password="1234",
    host="localhost",
    port="5432",
    options="-c client_encoding=utf8"  # Устанавливаем кодировку подключения
)

cursor = conn.cursor()

# Путь к файлу
file_path = "./City_List.csv"

# Переводим данные из Windows-1252 в UTF-8 и сохраняем в новый файл
with open("City_List.csv", mode='r', encoding='windows-1252') as infile:
    with open("City_List_utf8.csv", mode='w', encoding='utf-8', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        for row in reader:
            writer.writerow(row)

# Теперь загружаем данные из нового файла в базу данных
with open("City_List_utf8.csv", mode='r', encoding='utf-8') as infile:
    csv_reader = csv.reader(infile)
    next(csv_reader)  # Пропускаем заголовок
    for row in csv_reader:
        if len(row) < 4:  # Если в строке меньше 4 столбцов, пропускаем
            continue
        city_name = row[0].strip()
        country = row[1].strip()
        population = int(row[2].strip()) if row[2].strip().isdigit() else None
        area = float(row[3].strip()) if row[3].strip() else None

        # Проверяем, что все значения корректны
        if city_name and country and population:
            print(f"Добавляем в таблицу: {country}, {city_name}, {population}, {area}")
            cursor.execute(
                 "INSERT INTO city (city_name, country, population, area) VALUES (%s, %s, %s, %s)",
                    (city_name, country, population, area)
                
            )
        else:
            print(f"Пропускаем строку из-за некорректных данных: {row}")

# Фиксируем изменения и закрываем соединение
conn.commit()
cursor.close()
conn.close()

print("Данные успешно загружены!")
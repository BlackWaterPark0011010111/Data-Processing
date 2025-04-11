import psycopg2
import csv

#                  chcp 65001
#                 SET client_encoding = 'UTF8';
# CONNECTION PARAMETERS / ПАРАМЕТРЫ ПОДКЛЮЧЕНИЯ
conn = psycopg2.connect(
    dbname="city",
    user="postgres",
    password="1234",
    host="localhost",
    port="5432",
    options="-c client_encoding=utf8"  # SET ENCODING установка кодировки
)

cursor = conn.cursor()

file_path = "./City_List.csv"

# CONVERT DATA FROM WINDOWS-1252 TO UTF-8 AND SAVE TO NEW FILE
# перевод данных из windows в utf и сохранить в новый файл
with open("City_List.csv", mode='r', encoding='windows-1252') as infile:
    with open("City_List_utf8.csv", mode='w', encoding='utf-8', newline='') as outfile:

        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        for row in reader:
            writer.writerow(row)

#NOW LOAD DATA FROM NEW FILE TO DATABASE
#ЗАГРУЖАЕМ ДАННЫЕ ИЗ НОВОГО ФАЙЛА В БАЗУ ДАННЫХ
with open("City_List_utf8.csv", mode='r', encoding='utf-8') as infile:
    csv_reader = csv.reader(infile)
    next(csv_reader)  # SKIP HEADER ПРОПУСКАЕМ ЗАГОЛОВОК
    for row in csv_reader:
        if len(row) < 4:  # IF ROW HAS LESS THAN 4 COLUMNS, SKIP / ЕСЛИ В СТРОКЕ МЕНЬШЕ 4 СТОЛБЦОВ, ПРОПУСКАЕМ
            continue
        city_name = row[0].strip()
        country = row[1].strip()
        population = int(row[2].strip()) if row[2].strip().isdigit() else None
        area = float(row[3].strip()) if row[3].strip() else None

        # CHECK IF ALL VALUES ARE VALID
        # ПРОВЕРЯЕМ, ЧТО ВСЕ ЗНАЧЕНИЯ КОРРЕКТНЫ
        if city_name and country and population:
            print(f"ADDING TO TABLE: {country.upper()}, {city_name.upper()}, {population}, {area}")
            cursor.execute(
                "INSERT INTO city (city_name, country, population, area) VALUES (%s, %s, %s, %s)",
                (city_name, country, population, area)
            )
        else:
            print(f"SKIPPING ROW DUE TO INVALID DATA: {row}")

# COMMIT CHANGES AND CLOSE CONNECTION
# ФИКСИРУЕМ ИЗМЕНЕНИЯ И ЗАКРЫВАЕМ СОЕДИНЕНИЕ
conn.commit()
cursor.close()
conn.close()

print("DATA SUCCESSFULLY LOADED")
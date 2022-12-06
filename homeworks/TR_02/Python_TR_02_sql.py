#     С помощью SQL запросов через библиотеку sqlite создать таблицу содержаюую 2 стобца: номер и имя

import sqlite3

conn = sqlite3.connect(':memory:')
c = conn.cursor()
c.execute('''CREATE TABLE test_data
             (num integer PRIMARY KEY, name text NOT NULL)''')

#     Добавить три строки с данными.
c.executemany("INSERT INTO test_data VALUES (?,?);", [(1, 'Зенит'), (2, 'Спартак'), (3, 'ЦСКА')])
conn.commit()

#     Получить данные из таблицы и распечатать их на экране.

for row in c.execute('SELECT * FROM test_data'):
    print(row)

c.execute("SELECT * FROM test_data ORDER by length(name)")
print(c.fetchall())

conn.close()

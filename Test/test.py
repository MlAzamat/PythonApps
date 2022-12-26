import psycopg2
from psycopg2 import Error

def writefile(line):
    with open('C:\Github\PythonApps\Test\\text.txt', 'w') as file:
        file.write('\n'.join(line))

def get_table(id):

    try:
        # подключаемся к сущ Бд
        connection = psycopg2.connect(user='postgres',
            password='1111',
            host='localhost',
            port='5432',
            database='postgres')

        cursor = connection.cursor()
        postgreSQL_select_Query = "select * from foo where c1 = %s"

        result_value = cursor.execute(postgreSQL_select_Query, (id,))
        foo_records = cursor.fetchall()
        print(str(foo_records))
        return str(foo_records)

    except (Exception, Error) as error:
        print("Ошибка при работе с POstgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PG закрыто")
  
line = []
i = 1
for i in range(10):
    line = line + [get_table(i)]
    print(writefile(line))
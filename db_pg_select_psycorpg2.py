
import psycopg2
from psycopg2 import Error

def get_student_details(student_id):
    try:
        # подключаемся к сущ Бд
        connection = psycopg2.connect(user="postgres",
            password="1111",
            host="127.0.0.1",
            port="5432",
            database="postgres")

        cursor = connection.cursor()
        postgreSQL_select_Query = "select * from students where id = %s"

#Используйте cursor.execute() для выполнения запроса:
#cursor.fetchall() — для всех строк.
#cursor.fetchone() — для одной.
#cursor.fetchmany(SIZE) — для определенного количества.
#
#cursor.execute(postgreSQL_select_Query) - при выводе строк без условия where

        cursor.execute(postgreSQL_select_Query, (student_id,))
        print("Выбор строк из таблицы student с помощью cursor.fetchall")
        studetnts_records = cursor.fetchall()

        print("Вывод подходящей строки и её столбцов")
        for row in studetnts_records:
            print("id =", row[0], )
            print("fname =", row[1], )
            print("lname =", row[2], )
            print("pet =", row[3], "\n")
    
    except (Exception, Error) as error:
        print("Ошибка при работе с POstgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PG закрыто")
  
get_student_details(2)
get_student_details(3)
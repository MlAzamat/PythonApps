import psycopg2
from psycopg2 import Error

def put_student_details():
    try:
        # подключаемся к сущ Бд
        connection = psycopg2.connect(user="postgres",
            password="1111",
            host="127.0.0.1",
            port="5432",
            database="postgres")

        cursor = connection.cursor()
        # выполяем sql запрос insert 
        insert_query = """ INSERT INTO students(FNAME, LNAME, PET) VALUES
            ('Katya','Petrova','Nik'),
            ('Katrin','White','Jeck'),
            ('Miya','KII','Nice')"""
        cursor.execute(insert_query)
        connection.commit()

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")
  
put_student_details()
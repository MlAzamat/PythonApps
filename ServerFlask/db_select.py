import psycopg2
from psycopg2 import Error
import yaml
from yaml.loader import SafeLoader



def get_student_details(student_id):

    try:
        db = yaml.load(open('C:\Github\PythonApps\ServerFlask\db.yaml'),Loader=yaml.FullLoader)
        dbhost = db['pg_host']
        dbuser = db['pg_user']
        dbpassword = db['pg_password']
        dbdatabase = db['pg_db']
        dbport = db['pg_port']
        # подключаемся к сущ Бд
        connection = psycopg2.connect(user=dbuser,
            password=dbpassword,
            host=dbhost,
            port=dbport,
            database=dbdatabase)

        cursor = connection.cursor()
        postgreSQL_select_Query = "select * from students where id = %s"

# %S это 1 символ. иначе передавай список ['john']
#
#Используйте cursor.execute() для выполнения запроса:
#cursor.fetchall() — для всех строк.
#cursor.fetchone() — для одной.
#cursor.fetchmany(SIZE) — для определенного количества.
#
#cursor.execute(postgreSQL_select_Query) - при выводе строк без условия where

        result_value = cursor.execute(postgreSQL_select_Query, (student_id,))
      #  if result_value > 0:
        print("Выбор строк из таблицы student с помощью cursor.fetchall")
        studetnts_records = cursor.fetchall()
        print(str(studetnts_records))
        return str(studetnts_records)

    except (Exception, Error) as error:
        print("Ошибка при работе с POstgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PG закрыто")
  
#get_student_details(2)
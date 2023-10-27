import pymysql
import os
from dotenv import load_dotenv

load_dotenv()


def mysql_db():
    try:

        conn = pymysql.connect(
                        database=os.getenv("NAME"),
                        user=os.getenv("USER"),
                        host=os.getenv('HOST'),
                        password=os.getenv('PASSWORD'),
                        port=3306,
                        charset='utf8'
                        )

        return conn

    except Exception as e:
        print(f"Error: {e}")


# mysql_db()


def get_zakaz_materials():
    cursor = mysql_db().cursor()
    cursor.execute('SELECT * FROM zakaz_materials')
    rows = cursor.fetchall()
    for zakaz in rows:
        print(zakaz)


# get_zakaz_materials()


def get_all_columns_zakaz():
    cursor = mysql_db().cursor()
    cursor.execute("show columns from zakaz_materials")
    rows = cursor.fetchall()
    for row in rows:
        print(row)


# get_all_columns_zakaz()


def get_plan():
    cursor = mysql_db().cursor()
    cursor.execute('select remark from zakaz_materials')
    rows = cursor.fetchall()
    for row in rows:
        print(row[0])


# get_plan()


def get_all_info():
    cursor = mysql_db().cursor()
    cursor.execute('select id_material_category, remark, id_unit, xCount, date_zakaz_plan, is_plan, status, user_name from zakaz_materials')
    rows = cursor.fetchall()
    rows_list = []
    for row in rows:   
        # if int(row[6]) == 2:  # тут пусто когда статус равен 2
        rows_list.append(row)

    return rows_list


# print(get_all_info())

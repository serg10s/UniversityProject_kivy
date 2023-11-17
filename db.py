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


def get_all_info():
    cursor = mysql_db().cursor()
    cursor.execute('select id_material_category, remark, id_unit, xCount, date_zakaz_plan, is_plan, status, user_name from zakaz_materials')
    rows = cursor.fetchall()
    rows_list = []
    for row in rows:
        if row[6] != 3:
            rows_list.append(row)

    return rows_list

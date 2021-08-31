import pymysql
import dbconfig

connection = pymysql.connect(host=dbconfig.host,
                            user=dbconfig.db_user,
                            passwd=dbconfig.db_password)

try:
    with connection.cursor() as cursor:
        sql = "CREATE DATABASE IF NOT EXISTS checkmarx"
        cursor.execute(sql)

        sql = """CREATE TABLE IF NOT EXISTS checkmarx.users (
            id int NOT NULL AUTO_INCREMENT,
            user VARCHAR(50),
            password VARCHAR(50),
            PRIMARY KEY (id)
        )"""
        cursor.execute(sql)

        # clear out any old data
        sql = "DELETE FROM checkmarx.users"
        cursor.execute(sql)

        # create some test data
        sql = """INSERT INTO checkmarx.users (user, password) values ('Bugs', 'troz')"""
        cursor.execute(sql)
        sql = """INSERT INTO checkmarx.users (user, password) values ('Marvin', 'poit')"""
        cursor.execute(sql)
        sql = """INSERT INTO checkmarx.users (user, password) values ('Daffy', 'zort')"""
        cursor.execute(sql)
        
    connection.commit()
finally:
    connection.close()
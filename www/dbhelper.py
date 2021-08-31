import dbconfig
import pymysql
import sys

class DBHelper:

    def connect(self, database='checkmarx'):
        return pymysql.connect(host=dbconfig.host,
                                user=dbconfig.db_user,
                                passwd=dbconfig.db_password,
                                db=database)
    
    def select(self, query):
        connection = self.connect()
        try:
            with connection.cursor() as cursor:
                cursor.execute(query)
                return cursor.fetchall()
        finally:
            connection.close()
    
    def insert(self, query):
        connection = self.connect()
        try:
            with connection.cursor() as cursor:
                cursor.execute(query)
                connection.commit()
        finally:
            connection.close()
import mysql.connector

class Closer:
    def __init__(self, closeable):
        self.__closeable = closeable
    def __enter__(self):
        return self.__closeable
    def __exit__(self, exception_type, exception_value, exception_traceback):
        self.__closeable.close()
        return False

        def con():
            return mysql.connector.connect(
            host = "localhost",
            user = "admin",
            password = "#Adm123",
            database = "flaskapp")

#linha para usar o conector
#with Closer(con()) as connection, Closer(connection.cursor()) as cursor:
''' cursor.execute(
				'SELECT texto \
				FROM escolhas \
				WHERE storyID = {} \
				AND storyPart = {} '\
				.format(story, part))
    rows = cursor.fetchall()
    ou para colocar no banco connection.commit()
'''

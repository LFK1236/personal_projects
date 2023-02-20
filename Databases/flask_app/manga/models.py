from datetime import datetime, timedelta
from manga import connection
from psycopg2 import sql

class Main():
    def __init__(self):
        self.id = 0

class Volume(tuple):
    def __init__(self, volume_data):
        self.id = volume_data[0]
        self.name = volume_data[1]
        self.publish_date = volume_data[2]
        self.author = volume_data[3]
        self.entry = volume_data[4]

class Series(tuple):
    def __init__(self, series_data):
        self.name = series_data[0]
        self.author = series_data[1]

class Author(tuple):
    def __init__(self, author_data):
        self.name = author_data[0]

def select_Volumes():
    cursor = connection.cursor()
    sql = """
    SELECT * FROM Volumes
    """
    cursor.execute(sql)
    results = cursor.fetchall()
    cursor.close()
    volumes = []
    for vol in results:
        volumes.append(Volume(vol))
    return volumes

def add_Volume(input_data):
    cursor = connection.cursor()
    user_sql = sql.SQL ("""
    INSERT INTO Volumes(name, entry, author)
    VALUES(%s, %s, %s)
    """)
    cursor.execute(user_sql, (input_data[0], int(input_data[1]), input_data[2]))
    connection.commit()
    cursor.close()

def remove_Volume(id):
    cursor = connection.cursor()
    user_sql = sql.SQL ("""
    DELETE FROM Volumes
    WHERE id=%s
    """)
    cursor.execute(user_sql, (id,))
    connection.commit()
    cursor.close()

def select_Series():
    cursor = connection.cursor()
    sql = """
    SELECT DISTINCT name,author FROM Volumes
    """
    cursor.execute(sql)
    results = cursor.fetchall()
    cursor.close()
    series = []
    for ser in results:
        series.append(Series(ser))
    return series

def select_specific_Authors(name):
    cursor = connection.cursor()
    user_sql = sql.SQL ("""
    SELECT name FROM Authors
    WHERE name=%s
    """)
    cursor.execute(user_sql, (name,))
    results = cursor.fetchall()
    cursor.close()
    authors = []
    for author in results:
        authors.append(Author(author))
    return authors

def add_Author(name):
    cursor = connection.cursor()
    user_sql = sql.SQL ("""
    INSERT INTO Authors(name)
    VALUES(%s)
    """)
    cursor.execute(user_sql, (name,))
    connection.commit()
    cursor.close()
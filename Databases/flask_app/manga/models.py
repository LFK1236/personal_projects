from datetime import datetime, timedelta
from manga import connection
from psycopg2 import sql

class Main():
    def __init__(self):
        self.id = 0

class Volume(tuple):
    def __init__(self, volume_data):
        self.name = volume_data[0]
        self.series_year = volume_data[1]
        self.author = volume_data[2]
        self.entry = volume_data[3]

class Series(tuple):
    def __init__(self, series_data):
        self.name = series_data[0]
        self.author = series_data[1]
        self.series_year = series_data[2]

class Author(tuple):
    def __init__(self, author_data):
        self.name = author_data[0]

def select_Volumes():
    cursor = connection.cursor()
    sql = """
    SELECT Volumes.name,Volumes.series_year,Authorship.author,entry FROM Volumes LEFT JOIN Authorship ON Volumes.name=Authorship.series
    """
    cursor.execute(sql)
    results = cursor.fetchall()
    cursor.close()
    volumes = []
    for vol in results:
        volumes.append(Volume(vol))
    return volumes

def add_Volume(user_input):
    cursor = connection.cursor()
    user_sql = sql.SQL ("""
    INSERT INTO Volumes(name, entry, series_year)
    VALUES(%s, %s, %s)
    """)
    cursor.execute(user_sql, (user_input[0], int(user_input[1]), user_input[2]))
    connection.commit()
    cursor.close()

def remove_Volume(input):
    cursor = connection.cursor()
    user_sql = sql.SQL ("""
    DELETE FROM Volumes
    WHERE name=%s AND series_year=%s AND entry=%s
    """)
    cursor.execute(user_sql, (input[0], input[1], input[2]))
    connection.commit()
    cursor.close()

def select_Series():
    cursor = connection.cursor()
    sql = """
    SELECT Series.name,Authorship.author,Series.series_year FROM Series
    LEFT JOIN Authorship ON Series.name = Authorship.series
    """
    cursor.execute(sql)
    results = cursor.fetchall()
    cursor.close()
    series = []
    for ser in results:
        series.append(Series(ser))
    return series

def add_Series(user_input):
    cursor = connection.cursor()
    user_sql = sql.SQL ("""
    INSERT INTO Series(name, series_year)
    VALUES(%s, %s)
    """)
    cursor.execute(user_sql, (user_input[0], user_input[1]))
    connection.commit()
    cursor.close()

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
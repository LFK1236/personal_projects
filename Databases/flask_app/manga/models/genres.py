from manga import connection
from psycopg2 import sql

def select_Genres():
    cursor = connection.cursor()
    sql = """
    SELECT genre FROM Genres
    ORDER BY genre
    """
    cursor.execute(sql)
    genres = cursor.fetchall()
    cursor.close()
    genre_list = []
    for g in genres:
        genre_list.append(g)
    return genre_list

def add_Genre(name):
    cursor = connection.cursor()
    user_sql = sql.SQL ("""
    INSERT INTO Genres(genre)
    VALUES(%s)
    """)
    cursor.execute(user_sql, (name,))
    connection.commit()
    cursor.close()

def delete_Genre(name):
    cursor = connection.cursor()
    user_sql = sql.SQL ("""
    DELETE FROM Genres
    WHERE genre=%s
    """)
    cursor.execute(user_sql, (name,))
    connection.commit()
    cursor.close()

def add_Genre_Connection(input):
    cursor = connection.cursor()
    user_sql = sql.SQL ("""
    INSERT INTO Genre_Of(series, series_year, genre)
    VALUES (%s, %s, %s)
    """)
    cursor.execute(user_sql, (input[0], input[1], input[2]))
    connection.commit()
    cursor.close()

def select_Genres_by_Series(input):
    cursor = connection.cursor()
    user_sql = sql.SQL ("""
    SELECT genre FROM Genre_Of
    WHERE series=%s AND series_year=%s
    ORDER BY genre ASC
    """)
    cursor.execute(user_sql, (input[0], input[1]))
    results = cursor.fetchall()
    cursor.close()
    genre_list = []
    for r in results:
        genre_list.append(r[0])
    return genre_list

def delete_Genre_Connection(input):
    cursor = connection.cursor()
    user_sql = sql.SQL ("""
    DELETE FROM Genre_Of
    WHERE series=%s AND series_year=%s AND genre=%s
    """)
    cursor.execute(user_sql, (input[0], input[1], input[2]))
    connection.commit()
    cursor.close()
from datetime import datetime, timedelta
from manga import connection
from psycopg2 import sql

class Main():
    def __init__(self):
        self.id = 0

class Volume_Key(tuple):
    def __init__(self, volume_data):
        self.name = volume_data[0]
        self.series_year = volume_data[1]
        self.entry = volume_data[2]

class Volume():
    def __init__(self, Volume_Key, authors):
        self.name = Volume_Key.name
        self.series_year = Volume_Key.series_year
        self.entry = Volume_Key.entry
        self.authors = authors

"""
class Series(tuple):
    def __init__(self, series_data):
        self.name = series_data[0]
        self.author = series_data[1]
        self.series_year = series_data[2]
"""

class Series_Key(tuple):
    def __init__(self, series_data):
        self.name = series_data[0]
        self.series_year = series_data[1]

class Series():
    def __init__(self, key, authors):
        self.name = key[0]
        self.series_year = key[1]
        self.authors = authors

class Author(tuple):
    def __init__(self, author_data):
        self.name = author_data[0]

class Series_Full(tuple):
    def __init__(self, series_data):
        self.name = series_data[0]
        self.series_year = series_data[1]
        self.author = series_data[2]
        self.edition = series_data[3]
        self.language = series_data[4]
        self.rating = series_data[5]
        self.demographic = series_data[6]

class Authors(tuple):
    def __init__(self, author_data):
        self.name = author_data[0]

def select_Volumes():
    cursor = connection.cursor()
    sql = """
    SELECT Volumes.name, Volumes.series_year, entry
    FROM Volumes
    ORDER BY Volumes.name ASC
    """
    cursor.execute(sql)
    results = cursor.fetchall()
    volumes = []
    for vol in results:
        volumes.append(Volume_Key(vol))

    final_results = []
    for r in volumes:
        user_sql = ("""
        SELECT author FROM Authorship WHERE series=%s AND series_year=%s
        ORDER BY author ASC
        """)
        print(type(r))
        cursor.execute(user_sql, (r.name, r.series_year))
        authors = cursor.fetchall()
        author_list = []
        for a in authors:
            author_list.append(a[0])
        final_results.append(Volume(r, author_list))

    cursor.close()
    return final_results

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

def add_Series(user_input):
    cursor = connection.cursor()
    user_sql = sql.SQL ("""
    INSERT INTO Series(name, series_year)
    VALUES(%s, %s)
    """)
    cursor.execute(user_sql, (user_input[0], user_input[1]))
    connection.commit()
    cursor.close()

def select_Specific_Authors(name):
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

def select_Authors():
    cursor = connection.cursor()
    sql = """
    SELECT name FROM Authors
    ORDER BY name ASC
    """
    cursor.execute(sql)
    results = cursor.fetchall()
    cursor.close()
    authors = []
    for author in results:
        authors.append(Author(author))
    return authors

def delete_Author(name):
    cursor = connection.cursor()
    user_sql = sql.SQL ("""
    DELETE FROM Authors
    WHERE name=%s
    """)
    cursor.execute(user_sql, (name,))
    connection.commit()
    cursor.close()

def delete_Series(input):
    cursor = connection.cursor()
    user_sql = sql.SQL ("""
    DELETE FROM Series
    WHERE name=%s AND series_year=%s
    """)
    cursor.execute(user_sql, (input[0], input[1]))
    connection.commit()
    cursor.close()

def select_Specific_Series(input):
    cursor = connection.cursor()
    user_sql = sql.SQL ("""
    SELECT Series.name, Series.series_year, Authorship.author, edition, language, rating, demographic
    FROM Series LEFT JOIN Authorship ON Series.name=Authorship.series AND Series.series_year=Authorship.series_year
    WHERE Series.name=%s AND Series.series_year=%s
    """)
    cursor.execute(user_sql, (input[0], input[1]))
    results = cursor.fetchall()
    cursor.close()
    series = []
    for s in results:
        series.append(Series_Full(s))
    return series

def select_Authors_of_Series(input):
    cursor = connection.cursor()
    user_sql = sql.SQL ("""
    SELECT author FROM Authorship WHERE series=%s AND series_year=%s
    ORDER BY author ASC
    """)
    cursor.execute(user_sql, (input[0], input[1]))
    results = cursor.fetchall()
    cursor.close()
    names = []
    for author in results:
        names.append(Authors(author))
    return names

def select_Series_by_Author(name):
    cursor = connection.cursor()
    user_sql = sql.SQL ("""
    SELECT series, series_year FROM Authorship WHERE author=%s
    ORDER BY series, series_year, author ASC
    """)
    cursor.execute(user_sql, (name,))
    results = cursor.fetchall()
    series = []
    for s in results:
        series.append(Series_Key(s))
    
    final_results = []
    for s in series:
        user_sql = ("""
        SELECT author FROM Authorship WHERE series=%s AND series_year=%s
        ORDER BY author ASC
        """)
        cursor.execute(user_sql, (s.name, s.series_year))
        authors = cursor.fetchall()
        author_list = []
        for a in authors:
            author_list.append(a[0])
        final_results.append(Series(s, author_list))

    cursor.close()
    return final_results

def add_Authorship(input):
    cursor = connection.cursor()
    user_sql = sql.SQL ("""
    INSERT INTO Authorship(series, series_year, author)
    VALUES (%s, %s, %s)
    """)
    cursor.execute(user_sql, ([input[0], input[1], input[2]]))
    connection.commit()
    cursor.close()

def select_Series():
    cursor = connection.cursor()
    sql = """
    SELECT name, series_year FROM Series
    ORDER BY name, series_year ASC
    """
    cursor.execute(sql)
    results = cursor.fetchall()
    series = []
    for r in results:
        series.append(Series_Key(r))
    
    final_results = []
    for s in series:
        user_sql = ("""
        SELECT author FROM Authorship WHERE series=%s AND series_year=%s
        ORDER BY author ASC
        """)
        cursor.execute(user_sql, (s.name, s.series_year))
        authors = cursor.fetchall()
        author_list = []
        for a in authors:
            author_list.append(a[0])
        final_results.append(Series(s, author_list))

    cursor.close()
    return final_results

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

def select_Series_by_Genre(genre):
    cursor = connection.cursor()
    user_sql = sql.SQL ("""
    SELECT series, series_year FROM Genre_Of
    WHERE genre=%s
    ORDER BY series, series_year ASC
    """)
    cursor.execute(user_sql, (genre,))
    results = cursor.fetchall()
    series = []
    for r in results:
        series.append(Series_Key(r))
    
    final_results = []
    for s in series:
        user_sql = ("""
        SELECT author FROM Authorship WHERE series=%s AND series_year=%s
        ORDER BY author ASC
        """)
        cursor.execute(user_sql, (s.name, s.series_year))
        authors = cursor.fetchall()
        author_list = []
        for a in authors:
            author_list.append(a[0])
        final_results.append(Series(s, author_list))

    cursor.close()
    return final_results

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

def delete_Author_Connection(input):
    cursor = connection.cursor()
    user_sql = sql.SQL ("""
    DELETE FROM Authorship
    WHERE series=%s AND series_year=%s AND author=%s
    """)
    cursor.execute(user_sql, (input[0], input[1], input[2]))
    connection.commit()
    cursor.close()
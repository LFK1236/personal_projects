from manga import connection
from psycopg2 import sql

from manga.models.classes import Series_Key, Series_Full, Series

def add_Series(user_input):
    cursor = connection.cursor()
    user_sql = sql.SQL ("""
    INSERT INTO Series(name, series_year)
    VALUES(%s, %s)
    """)
    cursor.execute(user_sql, (user_input[0], user_input[1]))
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
    SELECT Series.name, Series.series_year, Authorship.author, edition, rating, language, demo, publisher
    FROM (Series LEFT JOIN Authorship ON Series.name=Authorship.series AND Series.series_year=Authorship.series_year)
    LEFT JOIN Language_Of
    ON Series.name=Language_Of.series AND Series.series_year=Language_Of.series_year
    LEFT JOIN Demographic_Of
    ON Series.name=Demographic_Of.series AND Series.series_year=Demographic_Of.series_year
    LEFT JOIN Publisher_Of
    ON Series.name=Publisher_Of.series AND Series.series_year=Publisher_Of.series_year
    WHERE Series.name=%s AND Series.series_year=%s
    """)
    cursor.execute(user_sql, (input[0], input[1]))
    results = cursor.fetchall()
    cursor.close()
    series = []
    for s in results:
        series.append(Series_Full(s))
    return series

def select_Series_by_Author(name):
    cursor = connection.cursor()
    user_sql = sql.SQL ("""
    SELECT Authorship.series, Authorship.series_year, COUNT(entry) FROM Authorship
    LEFT JOIN Volumes
    ON Authorship.series=Volumes.name AND Authorship.series_year=Volumes.series_year
    WHERE author=%s
    GROUP BY (Authorship.series, Authorship.series_year, author)
    ORDER BY Authorship.series, Authorship.series_year, author ASC
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

def select_Series():
    cursor = connection.cursor()
    sql = """
    SELECT Series.name, Series.series_year, COUNT(entry)
    FROM Series LEFT JOIN Volumes
    ON Series.name=Volumes.name AND Series.series_year=Volumes.series_year
    GROUP BY (Series.name, Series.series_year)
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

def select_Series_by_Genre(genre):
    cursor = connection.cursor()
    user_sql = sql.SQL ("""
    SELECT Genre_Of.series, Genre_Of.series_year, COUNT(entry) FROM Genre_Of
    LEFT JOIN Volumes ON Genre_Of.series=Volumes.name AND Genre_Of.series_year=Volumes.series_year
    WHERE genre=%s
    GROUP BY (Genre_Of.series, Genre_Of.series_year, genre)
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

def select_Series_by_Language(language):
    cursor = connection.cursor()
    user_sql = sql.SQL ("""
    SELECT Language_Of.series, Language_Of.series_year, COUNT(entry) FROM Language_Of
    LEFT JOIN Volumes ON Language_Of.series=Volumes.name AND Language_Of.series_year=Volumes.series_year
    WHERE language=%s
    GROUP BY (Language_Of.series, Language_Of.series_year)
    """)
    cursor.execute(user_sql, (language,))
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

def select_Series_by_Demographic(demographic):
    cursor = connection.cursor()
    user_sql = sql.SQL ("""
    SELECT Demographic_Of.series, Demographic_Of.series_year, COUNT(entry) FROM Demographic_Of
    LEFT JOIN Volumes ON Demographic_Of.series=Volumes.name AND Demographic_Of.series_year=Volumes.series_year
    WHERE demo=%s
    GROUP BY (Demographic_Of.series, Demographic_Of.series_year)
    """)
    cursor.execute(user_sql, (demographic,))
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

def select_Series_by_Publisher(publisher):
    cursor = connection.cursor()
    user_sql = sql.SQL ("""
    SELECT Publisher_Of.series, Publisher_Of.series_year, COUNT(entry)
    FROM Publisher_Of LEFT JOIN Volumes
    ON Publisher_Of.series=Volumes.name AND Publisher_Of.series_year=Volumes.series_year
    WHERE publisher=%s
    GROUP BY (Publisher_Of.series, Publisher_Of.series_year)
    """)
    cursor.execute(user_sql, (publisher,))
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
from manga import connection
from psycopg2 import sql

from manga.models.classes import Series, Series_Full, Series_with_Authors

def select_Series(sort):
    cursor = connection.cursor()
    if (sort.category == 'name, series_year' and sort.direction == 'DES'):
        print("desc")
        sql = """
        SELECT Series.name, Series.series_year, COUNT(entry), Series.rating
        FROM Series LEFT JOIN Volumes
        ON Series.name=Volumes.name AND Series.series_year=Volumes.series_year
        GROUP BY (Series.name, Series.series_year)
        ORDER BY name DESC, series_year DESC
        """
    elif (sort.category == 'rating' and sort.direction == 'ASC'):
        sql = """
        SELECT Series.name, Series.series_year, COUNT(entry), Series.rating
        FROM Series LEFT JOIN Volumes
        ON Series.name=Volumes.name AND Series.series_year=Volumes.series_year
        GROUP BY (Series.name, Series.series_year)
        ORDER BY Series.rating ASC, name ASC, series_year ASC
        """
    elif (sort.category == 'rating' and sort.direction == 'DES'):
        sql = """
        SELECT Series.name, Series.series_year, COUNT(entry), Series.rating
        FROM Series LEFT JOIN Volumes
        ON Series.name=Volumes.name AND Series.series_year=Volumes.series_year
        GROUP BY (Series.name, Series.series_year)
        ORDER BY Series.rating DESC, name DESC, series_year DESC
        """
    elif (sort.category == 'owned' and sort.direction == 'ASC'):
        sql = """
        SELECT Series.name, Series.series_year, COUNT(entry), Series.rating
        FROM Series LEFT JOIN Volumes
        ON Series.name=Volumes.name AND Series.series_year=Volumes.series_year
        GROUP BY (Series.name, Series.series_year)
        ORDER BY COUNT(entry) ASC, name ASC, series_year ASC
        """
    elif (sort.category == 'owned' and sort.direction == 'DES'):
        sql = """
        SELECT Series.name, Series.series_year, COUNT(entry), Series.rating
        FROM Series LEFT JOIN Volumes
        ON Series.name=Volumes.name AND Series.series_year=Volumes.series_year
        GROUP BY (Series.name, Series.series_year)
        ORDER BY COUNT(entry) DESC, name DESC, series_year DESC
        """
    # The author sorts do not work as intended.
    elif (sort.category == 'authors' and sort.direction == 'ASC'):
        sql = """
        SELECT Series.name, Series.series_year, COUNT(entry), Series.rating, author
        FROM Series
        LEFT JOIN
            (SELECT * 
            FROM Authorship
            ORDER BY author ASC
            LIMIT 1) AS auth
        ON auth.series=Series.name AND auth.series_year=Series.series_year
        LEFT JOIN Volumes
        ON Series.name=Volumes.name AND Series.series_year=Volumes.series_year
        GROUP BY (Series.name, Series.series_year, author)
        ORDER BY author ASC, Series.name ASC, Series.series_year ASC
        """
    elif (sort.category == 'authors' and sort.direction == 'DES'):
        sql = """
        SELECT Series.name, Series.series_year, COUNT(entry), Series.rating, author
        FROM Series
        LEFT JOIN
            (SELECT * 
            FROM Authorship
            ORDER BY author ASC
            LIMIT 1) AS auth
        ON auth.series=Series.name AND auth.series_year=Series.series_year
        LEFT JOIN Volumes
        ON Series.name=Volumes.name AND Series.series_year=Volumes.series_year
        GROUP BY (Series.name, Series.series_year, author)
        ORDER BY author DESC, Series.name ASC, Series.series_year ASC
        """
    else:
        print("else")
        sql = """
        SELECT Series.name, Series.series_year, COUNT(entry), Series.rating
        FROM Series LEFT JOIN Volumes
        ON Series.name=Volumes.name AND Series.series_year=Volumes.series_year
        GROUP BY (Series.name, Series.series_year)
        ORDER BY name ASC, series_year ASC
        """
    cursor.execute(sql,)
    results = cursor.fetchall()
    series = []
    for r in results:
        series.append(Series(r))
    print(series[0].name)
    print(series[2].name)

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
        final_results.append(Series_with_Authors(s, author_list))

    cursor.close()
    return final_results

def add_Series(series, series_year):
    cursor = connection.cursor()
    user_sql = sql.SQL ("""
    INSERT INTO Series(name, series_year)
    VALUES(%s, %s)
    """)
    cursor.execute(user_sql, (series, series_year))
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
    SELECT Authorship.series, Authorship.series_year, COUNT(entry), Series.rating FROM Authorship
    LEFT JOIN Volumes ON Authorship.series=Volumes.name AND Authorship.series_year=Volumes.series_year
    LEFT JOIN Series ON Series.name=Authorship.series AND Series.series_year=Authorship.series_year
    WHERE author=%s
    GROUP BY (Authorship.series, Authorship.series_year, Series.rating)
    ORDER BY Authorship.series, Authorship.series_year ASC
    """)
    cursor.execute(user_sql, (name,))
    results = cursor.fetchall()
    series = []
    for s in results:
        series.append(Series(s))

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
        final_results.append(Series_with_Authors(s, author_list))

    cursor.close()
    return final_results

def select_Series_by_Genre(genre):
    cursor = connection.cursor()
    user_sql = sql.SQL ("""
    SELECT Genre_Of.series, Genre_Of.series_year, COUNT(entry), Series.rating FROM Genre_Of
    LEFT JOIN Volumes ON Genre_Of.series=Volumes.name AND Genre_Of.series_year=Volumes.series_year
    LEFT JOIN Series ON Series.name=Genre_Of.series AND Series.series_year=Genre_Of.series_year
    WHERE genre=%s
    GROUP BY (Genre_Of.series, Genre_Of.series_year, Series.rating)
    ORDER BY Genre_Of.series, Genre_Of.series_year ASC
    """)
    cursor.execute(user_sql, (genre,))
    results = cursor.fetchall()
    series = []
    for r in results:
        series.append(Series(r))

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
        final_results.append(Series_with_Authors(s, author_list))

    cursor.close()
    return final_results

def select_Series_by_Language(language):
    cursor = connection.cursor()
    user_sql = sql.SQL ("""
    SELECT Language_Of.series, Language_Of.series_year, COUNT(entry), Series.rating FROM Language_Of
    LEFT JOIN Volumes ON Language_Of.series=Volumes.name AND Language_Of.series_year=Volumes.series_year
    LEFT JOIN Series ON Series.name=Language_Of.series AND Series.series_year=Language_Of.series_year
    WHERE language=%s
    GROUP BY (Language_Of.series, Language_Of.series_year, Series.rating)
    ORDER BY Language_Of.series, Language_Of.series_year ASC
    """)
    cursor.execute(user_sql, (language,))
    results = cursor.fetchall()
    series = []
    for r in results:
        series.append(Series(r))

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
        final_results.append(Series_with_Authors(s, author_list))

    cursor.close()
    return final_results

def select_Series_by_Demographic(demographic):
    cursor = connection.cursor()
    user_sql = sql.SQL ("""
    SELECT Demographic_Of.series, Demographic_Of.series_year, COUNT(entry), Series.rating FROM Demographic_Of
    LEFT JOIN Volumes ON Demographic_Of.series=Volumes.name AND Demographic_Of.series_year=Volumes.series_year
    LEFT JOIN Series ON Series.name=Demographic_Of.series AND Series.series_year=Demographic_Of.series_year
    WHERE demo=%s
    GROUP BY (Demographic_Of.series, Demographic_Of.series_year, Series.rating)
    ORDER BY Demographic_Of.series, Demographic_Of.series_year ASC
    """)
    cursor.execute(user_sql, (demographic,))
    results = cursor.fetchall()
    series = []
    for r in results:
        series.append(Series(r))

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
        final_results.append(Series_with_Authors(s, author_list))

    cursor.close()
    return final_results

def select_Series_by_Publisher(publisher):
    cursor = connection.cursor()
    user_sql = sql.SQL ("""
    SELECT Publisher_Of.series, Publisher_Of.series_year, COUNT(entry), Series.rating FROM Publisher_Of
    LEFT JOIN Volumes ON Publisher_Of.series=Volumes.name AND Publisher_Of.series_year=Volumes.series_year
    LEFT JOIN Series ON Series.name=Publisher_Of.series AND Series.series_year=Publisher_Of.series_year
    WHERE publisher=%s
    GROUP BY (Publisher_Of.series, Publisher_Of.series_year, Series.rating)
    ORDER BY Publisher_Of.series, Publisher_Of.series_year ASC
    """)
    cursor.execute(user_sql, (publisher,))
    results = cursor.fetchall()
    series = []
    for r in results:
        series.append(Series(r))

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
        final_results.append(Series_with_Authors(s, author_list))

    cursor.close()
    return final_results

def check_Series_Exists(series, series_year):
    cursor = connection.cursor()
    user_sql = sql.SQL ("""
    SELECT * FROM Series
    WHERE name=%s AND series_year=%s
    """)
    cursor.execute(user_sql, (series, series_year))
    result = cursor.fetchone()
    cursor.close()
    return (result != None)

def series_Update_Edition(series, series_year, edition):
    cursor = connection.cursor()
    user_sql = sql.SQL ("""
    UPDATE Series
    SET edition=%s
    WHERE name=%s AND series_year=%s
    """)
    cursor.execute(user_sql, (edition, series, series_year))
    connection.commit()
    cursor.close()

def series_Update_Rating(series, series_year, rating):
    cursor = connection.cursor()
    user_sql = sql.SQL ("""
    UPDATE Series
    SET rating=%s
    WHERE name=%s AND series_year=%s
    """)
    cursor.execute(user_sql, (rating, series, series_year))
    connection.commit()
    cursor.close()
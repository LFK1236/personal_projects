from manga import connection
from psycopg2 import sql

from manga.models.series import Order_By
from manga.models.classes import Series, Series_with_Authors

def search(term, sort):
    cursor = connection.cursor()
    user_sql = sql.SQL ("""
    SELECT Series.name, Series.series_year, COUNT(entry), Series.rating FROM
    Series LEFT JOIN Volumes ON Series.name=Volumes.name AND Series.series_year=Volumes.series_year
    WHERE Series.name LIKE %s OR Series.series_year=%s
    GROUP BY (Series.name, Series.series_year, Series.rating)
    """
    + Order_By(sort))
    cursor.execute(user_sql, (term, term))
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
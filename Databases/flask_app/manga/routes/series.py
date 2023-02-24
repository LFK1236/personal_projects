from flask import render_template, url_for, redirect, Blueprint, request
from manga.models.series import select_Series, add_Series, delete_Series
from manga.models.series import select_Specific_Series, select_Series_by_Genre
from manga.models.authors import select_Authors_of_Series, connect_Author, delete_Author_Connection
from manga.models.genres import add_Genre_Connection, select_Genres_by_Series, delete_Genre_Connection
from manga.models.languages import connect_Language
from manga.models.demographics import connect_Demographic
from manga.models.publishers import connect_Publisher
from manga.models.series import select_Series_by_Language, select_Series_by_Demographic
from manga.models.series import select_Series_by_Publisher

Series = Blueprint('Manga Series', __name__)

@Series.route('/series', methods=['GET'])
def series():
    series = select_Series()
    return render_template('series.html', title='Manga Series', series=series)

@Series.route('/series/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        series = request.form['name']
        series_year = request.form['series_year']
        author = request.form['author']
        language = request.form['language']
        demographic = request.form['demographic']
        publisher = request.form['publisher']
        if series != "" and series_year != "":
            add_Series([series, series_year])
            connect_Author(series, series_year, author)
            connect_Language(series, series_year, language)
            connect_Demographic(series, series_year, demographic)
            connect_Publisher(series, series_year, publisher)

    return redirect('/series')

@Series.route('/series/delete', methods=['POST'])
def delete():
    if request.method == 'POST':
        volume_info = [request.form['name'], request.form['series_year']]
        delete_Series(volume_info)
        return redirect('/series')

@Series.route('/series/details/<string:series_name>/<string:series_year>', methods=['GET', 'POST'])
def details(series_name, series_year):
    series_info = [series_name, series_year]
    series = select_Specific_Series(series_info)
    names = select_Authors_of_Series(series_info)
    genres = select_Genres_by_Series(series_info)
    return render_template('series_details.html', title='Series Details', series=series[0], names=names, genres=genres)

@Series.route('/series/connect/author', methods=['POST'])
def connect_author():
    if request.method == 'POST':
        from_url = request.form['from']
        connect_Author(request.form['name'], request.form['series_year'], request.form['author_name'])
    return redirect(from_url)

@Series.route('/series/connect/genre', methods=['POST'])
def connect_genre():
    if request.method == 'POST':
        genre_connection = [request.form['name'], request.form['series_year'], request.form['genre_name']]
        from_url = request.form['from']
        add_Genre_Connection(genre_connection)
    return redirect(from_url)

@Series.route('/series/genre:<string:genre>', methods=['GET', 'POST'])
def series_by_genre(genre):
    series = select_Series_by_Genre(genre)
    return render_template('series_by_filter.html', title='Series', series=series, filter=genre)

@Series.route('/series/disconnect/genre', methods=['POST'])
def disconnect_genre():
    if request.method == 'POST':
        genre_info = [request.form['series_name'], request.form['series_year'], request.form['genre_name']]
        from_url = request.form['from']
        delete_Genre_Connection(genre_info)
    return redirect(from_url)

@Series.route('/series/disconnect/author', methods=['POST'])
def disconnect_author():
    if request.method == 'POST':
        authorship = [request.form['series_name'], request.form['series_year'], request.form['author_name']]
        from_url = request.form['from']
        delete_Author_Connection(authorship)
    return redirect(from_url)

@Series.route('/series/language:<string:language>', methods=['GET', 'POST'])
def series_by_language(language):
    series = select_Series_by_Language(language)
    return render_template('series_by_filter.html', title='Series', series=series, filter=language)

@Series.route('/series/demographic:<string:demographic>', methods=['GET', 'POST'])
def series_by_demographic(demographic):
    series = select_Series_by_Demographic(demographic)
    return render_template('series_by_filter.html', title='Series', series=series, filter=demographic)

@Series.route('/series/publisher:<string:publisher>', methods=['GET', 'POST'])
def series_by_publisher(publisher):
    series = select_Series_by_Publisher(publisher)
    return render_template('series_by_filter.html', title='Series', series=series, filter=publisher)
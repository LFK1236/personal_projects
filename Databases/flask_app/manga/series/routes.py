from flask import render_template, url_for, redirect, Blueprint, request
from manga.models import select_Series, add_Series, delete_Series
from manga.models import select_Specific_Series, select_Authors_of_Series, add_Authorship
from manga.models import select_Series_by_Genre, add_Genre_Connection, select_Genres_by_Series
from manga.models import delete_Genre_Connection, delete_Author_Connection, select_Language_of_Series

Series = Blueprint('Manga Series', __name__)

@Series.route('/series', methods=['GET'])
def series():
    series = select_Series()
    return render_template('series.html', title='Manga Series', series=series)

@Series.route('/series/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        series_info = [request.form['name'], request.form['series_year']]
        if series_info[0] != None and series_info[1] != None:
            add_Series(series_info)
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
        authorship = [request.form['name'], request.form['series_year'], request.form['author_name']]
        from_url = request.form['from']
        add_Authorship(authorship)
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
    return render_template('series_by_genre.html', title='Series', series=series, genre=genre)

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
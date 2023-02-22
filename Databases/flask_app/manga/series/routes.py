from flask import render_template, url_for, redirect, Blueprint, request
from manga.models import select_Series, add_Series, delete_Series, select_Specific_Series, select_Authors_of_Series, add_Authorship

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

@Series.route('/series/details', methods=['GET', 'POST'])
def details():
    if request.method == 'POST':
        series_info = [request.form['name'], request.form['series_year']]
        series = select_Specific_Series(series_info)
        names = select_Authors_of_Series(series_info)
        return render_template('series_details.html', title='Series Details', series=series[0], names=names)

@Series.route('/series/connect', methods=['POST'])
def connect():
    if request.method == 'POST':
        authorship = [request.form['name'], request.form['series_year'], request.form['author_name']]
        add_Authorship(authorship)
    return redirect('/series')
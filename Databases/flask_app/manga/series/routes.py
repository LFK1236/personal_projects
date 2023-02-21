from flask import render_template, url_for, redirect, Blueprint, request
from manga.models import select_Series, add_Series, delete_Series

Series = Blueprint('Manga Series', __name__)

@Series.route('/series', methods=['GET', 'POST'])
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
        print("entered delete route")
        volume_info = [request.form['name'], request.form['series_year']]
        delete_Series(volume_info)
        return redirect('/series')
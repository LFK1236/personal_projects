from flask import render_template, url_for, redirect, Blueprint, request
from manga.models import select_Series

Series_Manga = Blueprint('Manga Series', __name__)

@Series_Manga.route('/series', methods=['GET', 'POST'])
def series():
    series = select_Series()
    return render_template('series.html', title='Manga Series', series=series)
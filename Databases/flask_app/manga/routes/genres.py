from flask import render_template, url_for, redirect, Blueprint, request
from manga.models.genres import select_Genres, add_Genre, delete_Genre

Genres = Blueprint('Genres', __name__)

@Genres.route('/genres', methods=['GET'])
def genres():
    genres = select_Genres()
    return render_template('genres.html', title='Genres', genres=genres)

@Genres.route('/genres/add', methods=['POST'])
def add():
    new = request.form['genre_name']
    add_Genre(new)
    return redirect('/genres')

@Genres.route('/genres/delete', methods=['POST'])
def delete():
    genre = request.form['genre_name']
    delete_Genre(genre)
    return redirect('/genres')
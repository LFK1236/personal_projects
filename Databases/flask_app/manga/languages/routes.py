from flask import render_template, url_for, redirect, Blueprint, request
from manga.models import select_Languages, add_Language, delete_Language

Languages = Blueprint('Languages', __name__)

@Languages.route('/languages', methods=['GET'])
def languages():
    languages = select_Languages()
    return render_template('languages.html', title='Languages', languages=languages)

@Languages.route('/languages/add', methods=['POST'])
def add():
    language = request.form['language']
    add_Language(language)
    return redirect('/languages')

@Languages.route('/languages/delete', methods=['POST'])
def delete():
    language = request.form['language']
    delete_Language(language)
    return redirect('/languages')
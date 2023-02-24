from flask import render_template, url_for, redirect, Blueprint, request
from manga.models.publishers import select_Publishers, add_Publisher, delete_Publisher

Publishers = Blueprint('Publishers', __name__)

@Publishers.route('/publishers', methods=['GET'])
def publishers():
    publishers = select_Publishers()
    return render_template('publishers.html', title='Publishers', publishers=publishers)

@Publishers.route('/publishers/add', methods=['POST'])
def add():
    publisher = request.form['publisher']
    add_Publisher(publisher)
    return redirect('/publishers')

@Publishers.route('/publishers/delete', methods=['POST'])
def delete():
    publisher = request.form['publisher']
    delete_Publisher(publisher)
    return redirect('/publishers')
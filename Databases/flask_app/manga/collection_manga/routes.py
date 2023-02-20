from flask import render_template, url_for, redirect, Blueprint, request
from manga.models import select_Volumes, add_Volume, remove_Volume, select_specific_Authors, add_Author

Collection_Manga = Blueprint('Manga Collection', __name__)

@Collection_Manga.route('/collection', methods=['GET', 'POST'])
def collection():
    volumes = select_Volumes()
    return render_template('collection.html', title='Manga Collection', volumes=volumes)

@Collection_Manga.route('/collection/add', methods=['POST'])
def add():
    if request.method == 'POST':
        volume_info = [request.form['name'], request.form.get('entry', type=int), request.form['author']]
        if volume_info[0] != None and volume_info[2] != None:
            matching_authors = select_specific_Authors(volume_info[2])
            print(type(matching_authors))
            if (len(matching_authors) == 0):
                add_Author(volume_info[2])
            add_Volume(volume_info)
        return redirect('/collection')

@Collection_Manga.route('/collection/add/multiple', methods=['POST'])
def add_multiple():
    if request.method == 'POST':
        print('Reached post - insert multiple')
        volume_info = [request.form['name'], request.form['author'], 
            request.form.get('start_entry', type=int), request.form.get('entries', type=int)]

        if volume_info[2] != None and volume_info[3] != None and volume_info[3] > volume_info[2]:
            for entry in range(volume_info[2], volume_info[3] + 1):
                add_Volume([ volume_info[0], entry, volume_info[1] ])

        return redirect('/collection')

@Collection_Manga.route('/collection/delete', methods=['POST'])
def delete():
    if request.method == 'POST':
        remove_Volume([request.form['volume_id']][0])
        return redirect('/collection')
from flask import Flask
import psycopg2

app = Flask(__name__)
database = "dbname='mangadb' user='postgres' host='127.0.0.1' password = '123'"
connection = psycopg2.connect(database)

from manga.volumes.routes import Volumes
app.register_blueprint(Volumes)

from manga.splash.routes import Splash
app.register_blueprint(Splash)

from manga.series.routes import Series
app.register_blueprint(Series)

from manga.authors.routes import Authors
app.register_blueprint(Authors)

from manga.genres.routes import Genres
app.register_blueprint(Genres)

from manga.languages.routes import Languages
app.register_blueprint(Languages)

from manga.demographics.routes import Demographics
app.register_blueprint(Demographics)

from manga.publishers.routes import Publishers
app.register_blueprint(Publishers)
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
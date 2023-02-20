from flask import Flask
import psycopg2

app = Flask(__name__)
database = "dbname='mangadb' user='postgres' host='127.0.0.1' password = '123'"
connection = psycopg2.connect(database)

from manga.collection_manga.routes import Collection_Manga
app.register_blueprint(Collection_Manga)

from manga.splash.routes import Splash
app.register_blueprint(Splash)

from manga.series_manga.routes import Series_Manga
app.register_blueprint(Series_Manga)

'''
from MinSPFlask.Contact.routes import Contact
app.register_blueprint(Contact)

from MinSPFlask.Notification.routes import Notification
app.register_blueprint(Notification)

from MinSPFlask.Settings.routes import Settings
app.register_blueprint(Settings)

from MinSPFlask.Menu.routes import Menu
app.register_blueprint(Menu)
'''
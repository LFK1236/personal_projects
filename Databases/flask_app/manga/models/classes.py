class Volume_Key(tuple):
    def __init__(self, volume_data):
        self.name = volume_data[0]
        self.series_year = volume_data[1]
        self.entry = volume_data[2]

class Volume():
    def __init__(self, Volume_Key, authors):
        self.name = Volume_Key.name
        self.series_year = Volume_Key.series_year
        self.entry = Volume_Key.entry
        self.authors = authors

class Series(tuple):
    def __init__(self, series_data):
        self.name = series_data[0]
        self.series_year = series_data[1]
        self.volumes = series_data[2]
        self.rating = series_data[3]

class Series_with_Authors():
    def __init__(self, key, authors):
        self.name = key[0]
        self.series_year = key[1]
        self.volumes = key[2]
        self.rating = key[3]
        self.authors = authors

class Author(tuple):
    def __init__(self, author_data):
        self.name = author_data[0]

class Series_Full(tuple):
    def __init__(self, series_data):
        self.name = series_data[0]
        self.series_year = series_data[1]
        self.author = series_data[2]
        self.edition = series_data[3]
        self.rating = series_data[4]
        self.language = series_data[5]
        self.demographic = series_data[6]
        self.publisher = series_data[7]

class Authors(tuple):
    def __init__(self, author_data):
        self.name = author_data[0]

class Demographic(tuple):
    def __init__(self, demo_data):
        self.demo = demo_data[0]
        self.desc = demo_data[1]
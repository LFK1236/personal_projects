\i schema_drop.sql

CREATE TABLE IF NOT EXISTS Authors(
    name varchar(120) PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS Series(
    name varchar(120),
    series_year char(4),
    language varchar(30) DEFAULT 'English',
    edition varchar(120),
    rating integer DEFAULT 0,
    demographic varchar(120),
    PRIMARY KEY (name, series_year)
);

CREATE TABLE IF NOT EXISTS Authorship(
    author varchar(120),
    series varchar(120),
    series_year char(4),
    CONSTRAINT fk_author
        FOREIGN KEY (author)
        REFERENCES Authors(name),
    CONSTRAINT fk_series
        FOREIGN KEY (series, series_year)
        REFERENCES Series(name, series_year)
);

CREATE TABLE IF NOT EXISTS Volumes(
    name varchar(120) NOT NULL,
    series_year char(4),
    entry integer DEFAULT 1,
    isbn varchar(120) UNIQUE,
    read_status boolean DEFAULT FALSE,
    CONSTRAINT fk_series
        FOREIGN KEY (name, series_year)
        REFERENCES Series(name, series_year),
    PRIMARY KEY (entry, name, series_year)
);

CREATE TABLE IF NOT EXISTS Genres(
    genre varchar(120) PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS Genre_Of(
    genre varchar(120) REFERENCES Genres(genre),
    series varchar(120),
    series_year char(4),
    CONSTRAINT fk_series
        FOREIGN KEY (series, series_year)
        REFERENCES Series(name, series_year)
);
\i schema_drop.sql

CREATE SEQUENCE Vol_ID_seq;

CREATE TABLE IF NOT EXISTS Authors(
    name varchar(120) PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS Series(
    name varchar(120),
    series_year char(4),
    language varchar(30) DEFAULT 'English',
    edition varchar(120),
    publisher varchar(120), --TODO: refactor
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

-- I'd like to make the entry and foreign key constraint into one overall key somehow. Not sure how.
CREATE TABLE IF NOT EXISTS Volumes(
    ID integer DEFAULT nextval('Vol_ID_seq') PRIMARY KEY,
    name varchar(120) NOT NULL,
    series_year char(4),
    entry integer DEFAULT 1,
    isbn varchar(120) UNIQUE,
    read_status boolean DEFAULT FALSE,
    CONSTRAINT fk_nameyear
        FOREIGN KEY (name, series_year)
        REFERENCES Series(name, series_year)
);
\i schema_drop.sql

CREATE SEQUENCE Vol_ID_seq;

CREATE TABLE IF NOT EXISTS Authors(
    name varchar(120) PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS Volumes(
    ID integer DEFAULT nextval('Vol_ID_seq') PRIMARY KEY,
    name varchar(120) NOT NULL,
    publish_date char(10),
    author varchar(120),
    entry integer DEFAULT 1,
    language varchar(30) DEFAULT 'English', --Could be foreign key to a "languages" relation, but I don't have a strong argument either way
    isbn varchar(120) UNIQUE,
    publisher varchar(120),
    read_status boolean DEFAULT FALSE,
    CONSTRAINT fk_author
        FOREIGN KEY (author)
        REFERENCES Authors(name)
);

-- This and Volumes will have to be remade. This was all done off-the-cuff while literally feverish,
-- but upon actually taking 5 minutes to think through the schema, it shouldn't work like this.
CREATE TABLE IF NOT EXISTS Series(
    name varchar(120),
    author varchar(120),
    language varchar(30),
    rating integer DEFAULT 0
);
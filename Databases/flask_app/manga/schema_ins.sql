INSERT INTO Authors(name)
VALUES ('Akira Toriyama'), ('Eiichiro Oda'), ('Hiromu Arakawa');

INSERT INTO Series(name, series_year)
VALUES  ('Dragonball', '2003'),
        ('One Piece', '2003');

INSERT INTO Series(name, series_year, edition)
VALUES ('Fullmetal Alchemist', '2018', 'Fullmetal Edition');

INSERT INTO Authorship(author, series, series_year)
VALUES 
    ('Akira Toriyama', 'Dragonball', '2003'),
    ('Eiichiro Oda', 'One Piece', '2003'),
    ('Hiromu Arakawa', 'Fullmetal Alchemist', '2018');

INSERT INTO Volumes(name, series_year, entry)
VALUES
    ('Dragonball', '2003', 1),
    ('Dragonball', '2003', 2),
    ('Dragonball', '2003', 3),
    ('One Piece', '2003', 1);

INSERT INTO Genres(genre)
VALUES
    ('Adventure'), ('Action'), ('Martial Arts'), ('Wholesome'), ('Slice of Life'), ('Isekai'), ('Horror');

INSERT INTO Genre_Of(genre, series, series_year)
VALUES
    ('Adventure', 'Dragonball', '2003'), ('Action', 'Dragonball', '2003'), ('Martial Arts', 'Dragonball', '2003'),
    ('Adventure', 'One Piece', '2003'), ('Action', 'One Piece', '2003')
;
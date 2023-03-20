CREATE TABLE if not exists Games (
	title varchar(120),
	release_year char(4),
	rating int,
	PRIMARY KEY (title, release_year)
);

CREATE TABLE if not exists Platforms (
	platform varchar(120) PRIMARY KEY
);

CREATE TABLE if not exists Publishers (
	publisher varchar(120) PRIMARY KEY
);

CREATE TABLE if not exists Franchises (
	franchise varchar(120) PRIMARY KEY
);

CREATE TABLE if not exists Distributions (
	distribution_platform varchar(120) PRIMARY KEY
);

CREATE TABLE if not exists Developers (
	developer varchar(120) PRIMARY KEY
);

CREATE TABLE if not exists Genres (
	genre varchar(120) PRIMARY KEY
);

--
-- Relations
--

CREATE TABLE if not exists Platform_Of (
	platform REFERENCES Platforms(platform)
		ON DELETE CASCADE
		ON UPDATE CASCADE,
	title varchar(120),
	release_year char(4),
	CONSTRAINT fk_game
        FOREIGN KEY (title, release_year)
        REFERENCES Games(title, release_year)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE if not exists Publisher_Of (
	publisher REFERENCES Publishers(publisher)
		ON DELETE CASCADE
		ON UPDATE CASCADE,
	title varchar(120),
	release_year char(4),
	CONSTRAINT fk_game
        FOREIGN KEY (title, release_year)
        REFERENCES Games(title, release_year)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE if not exists Franchise_Of (
	franchise REFERENCES Franchises(franchise)
		ON DELETE CASCADE
		ON UPDATE CASCADE,
	title varchar(120),
	release_year char(4),
	CONSTRAINT fk_game
        FOREIGN KEY (title, release_year)
        REFERENCES Games(title, release_year)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE if not exists Distribution_Of (
	distribution_platform REFERENCES Distributions(distribution_platform)
		ON DELETE CASCADE
		ON UPDATE CASCADE,
	title varchar(120),
	release_year char(4),
	CONSTRAINT fk_game
        FOREIGN KEY (title, release_year)
        REFERENCES Games(title, release_year)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE if not exists Developer_Of (
	developer REFERENCES Developers(developer)
		ON DELETE CASCADE
		ON UPDATE CASCADE,
	title varchar(120),
	release_year char(4),
	CONSTRAINT fk_game
        FOREIGN KEY (title, release_year)
        REFERENCES Games(title, release_year)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE if not exists Genre_Of (
	genre REFERENCES Genres(genre)
		ON DELETE CASCADE
		ON UPDATE CASCADE,
	title varchar(120),
	release_year char(4),
	CONSTRAINT fk_game
        FOREIGN KEY (title, release_year)
        REFERENCES Games(title, release_year)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
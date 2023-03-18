CREATE TABLE IF NOT EXISTS Games (
	title varchar(120),
	release_year char(4),
	rating int,
	PRIMARY KEY (title, release_year)
);

CREATE TABLE IF NOT EXISTS Platforms (
	platform varchar(120) PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS Publishers (
	publisher varchar(120) PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS Franchises (
	franchise varchar(120) PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS Distributions (
	distribution_platform varchar(120) PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS Developers (
	developer varchar(120) PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS Genres (
	genre varchar(120) PRIMARY KEY
);

--
-- Relations
--

CREATE TABLE IF NOT EXISTS Platform_Of (
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

CREATE TABLE IF NOT EXISTS Publisher_Of (
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

CREATE TABLE IF NOT EXISTS Franchise_Of (
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

CREATE TABLE IF NOT EXISTS Distribution_Of (
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

CREATE TABLE IF NOT EXISTS Developer_Of (
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

CREATE TABLE IF NOT EXISTS Genre_Of (
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
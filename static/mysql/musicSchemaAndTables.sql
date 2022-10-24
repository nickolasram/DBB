DROP SCHEMA IF EXISTS `musicrating` ;

CREATE SCHEMA IF NOT EXISTS `musicrating` DEFAULT CHARACTER SET utf8 ;

USE musicrating;

CREATE TABLE artists (
artistid INT(10) NOT NULL AUTO_INCREMENT PRIMARY KEY,
artistname VARCHAR(100) NOT NULL,
artistnationality VARCHAR(100) NOT NULL,
artistbirthyear VARCHAR(5) DEFAULT '?');

ALTER TABLE artists
ADD plurality ENUM("individual", "group");

CREATE TABLE albums (
albumid INT(10) NOT NULL AUTO_INCREMENT,
albumtitle VARCHAR(100) NOT NULL,
artistid INT(10) NOT NULL,
albumyear INT(4) NOT NULL,
albumformat VARCHAR(5) NOT NULL,
songcount INT(3) NOT NULL,
PRIMARY KEY (albumID),
FOREIGN KEY (artistID) REFERENCES artists(artistID));

ALTER TABLE albums 
MODIFY albumformat ENUM("full", "EP", "single", "classical composition");

CREATE TABLE songs (
songid INT(10) NOT NULL AUTO_INCREMENT,
songtitle VARCHAR(100) NOT NULL,
albumid INT(10) NOT NULL,
genre SET("jazz", "blues", "folk", "rock", "metal", "pop", "hiphop", "classical", "international", "soul", "reggae") NOT NULL,
score INT(1) NOT NULL,
PRIMARY KEY (songid),
FOREIGN KEY (albumid) REFERENCES albums(albumid));
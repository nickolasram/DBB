INSERT INTO artists VALUES
-- id, name, nationality, birthyear, plurality
(NULL, 'Donny Hathaway', 'American', '1945', 'individual'),
(NULL, 'Curtis Harding', 'American', '1979', 'individual'),
(NULL, 'Matin Carthy', 'English', '1941', 'individual'),
(NULL, 'Coleman Hawkins', 'American', '1904', 'individual'),
(NULL, 'William Byrd', 'English', '~1540', 'individual'),
(NULL, 'Hozier', 'Irish', '1990', 'individual'),
(NULL, 'Snow', 'Canadian', '1969', 'individual'),
(NULL, 'Stromae', 'Belgian', '1985', 'individual'),
(NULL, 'Cannonball Adderly', 'American', '1928', 'individual'),
(NULL, 'Jimi Hendrix', 'American', '1942', 'individual'),
(NULL, 'Barcelona Gipsy Klezmer Orchestra', 'Spanish', '2012', 'group'),
(NULL, 'Duke Ellington', 'American', '1899', 'individual'),
(NULL, 'Hinder', 'American', '2001', 'group'),
(NULL, 'Disturbed', 'American', '1994', 'group');

INSERT INTO albums VALUES
-- id, title, artistid, year, format, count
(NULL, 'Donny Hathaway', 1, 1971, 'full', 11),
(NULL, 'Face Your Fear', 2, 2017, 'full', 11),
(NULL, 'Martin Carthy', 3, 1965, 'full', 14),
(NULL, 'Body and Soul', 4, 1939, 'full', 19),
(NULL, 'Mass for Five Voices', 5, 1593, 'classical composition', 5),
(NULL, 'Hozier', 6, 2014, 'full', 13),
(NULL, '12 Inches of Snow', 7, 1993, 'full', 14),
(NULL, 'Racine Carree', 8, 2013, 'full', 14),
(NULL, 'Mercy, Mercy, Mercy!  Live at "The Club', 9, 1967, 'full', 7),
(NULL, 'Band of Gypsys', 10, 1970, 'full', 9),
(NULL, 'Duke Ellington & John Coltrane', 12, 1963, 'full', 7),
(NULL, 'Imbarca', 11, 2013, 'full', 12),
(NULL, 'Soul Power', 2, 2014, 'full', 12),
(NULL, 'Electric Ladyland', 10, 1968, 'full', 19),
(NULL, "Somethin' Else", 9, 1958, 'full', 6),
(NULL, 'Concerto for Cootie', 12, 1940, 'EP', 2),
(NULL, 'Live', 1, 1972, 'full', 8),
(NULL, 'Extreme Behavior', 13, 2005, 'full', 12),
(NULL, 'Indestructible', 14, 2008, 'full', 12);

INSERT INTO songs VALUES
-- id, title, album id, genre, score
(NULL, 'A Song for You', 1, 'Soul', 7),
(NULL, 'Till the End', 2, 'Soul', 6),
(NULL, 'Scarborough Fair', 3, 'Folk', 6),
(NULL, 'Body and Soul', 4, 'Jazz', 7),
(NULL, 'V. Agnus Dei', 5, 'Classical', 7),
(NULL, 'Angel of Small Death and the Codeine Scene', 6, 'Rock', 5),
(NULL, 'Lady With the Red Dress On', 7, 'Hiphop', 5),
(NULL, 'Formidable', 8, 'Hiphop', 6),
(NULL, 'Mercy, Mercy, Mercy', 9, 'Jazz', 7),
(NULL, 'Machine Gun - Live', 10, 'Rock', 7),
(NULL, 'She is My Lady', 1, 'Soul', 7),
(NULL, 'Need Your Love', 2, 'Soul', 6),
(NULL, 'Work Song', 6, 'Rock', 6),
(NULL, 'Hevenu Shalom Alechem', 12, 'Folk', 6),
(NULL, 'Get Stoned', 18, 'Rock', 1),
(NULL, 'Indestructible', 19, 'Rock', 1);

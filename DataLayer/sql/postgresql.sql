DROP TABLE IF EXISTS users;
CREATE TABLE IF NOT EXISTS users (
    id_user CHAR(128) PRIMARY KEY NOT NULL,
    password_user CHAR(128) NOT NULL,
    favorite_type_beer CHAR(128) NOT NULL,
    budget_user float NOT NULL,
);

DROP TABLE IF EXISTS beers;
CREATE TABLE IF NOT EXISTS beers (
    name_beer VARCHAR(50) PRIMARY KEY NOT NULL,
    type_beer CHAR(128) NOT NULL,
);

DROP TABLE IF EXISTS pubs;
CREATE TABLE IF NOT EXISTS pubs (
    name_pub VARCHAR(50) PRIMARY KEY NOT NULL,
    localisation_pub VARCHAR(50) NOT NULL,
);

DROP TABLE IF EXISTS menu;
CREATE TABLE IF NOT EXISTS menu (
    price_beer float NOT NULL,
    FOREIGN KEY (name_beer) REFERENCES beers(name_beer)
    FOREIGN KEY (name_pub) REFERENCES pubs(name_pub)
);

INSERT INTO beers (name_beer, type_beer)
VALUES 
    ('Stella Artois', 'Blonde'),
    ('Corona', 'Blonde'), 
    ('Carlsberg', 'Blonde'),
    ('Guinness', 'Brune'), 
    ('Kronenbourg', 'Blonde'), 
    ('Desperados', 'Blonde'),
    ('Desperados Red', 'Rouge'),
    ('Hoegaarden', 'Blanche'), 
    ('Heineken', "Blonde"), 
    ('1664', 'Blonde'),
    ('1664 Blanche', 'Blanche'),
    ('Leffe', 'Blonde'), 
    ('Leffe Ruby', 'Rouge');

INSERT INTO
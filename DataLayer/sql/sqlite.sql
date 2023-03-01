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

DROP TABLE IF EXISTS menus;
CREATE TABLE IF NOT EXISTS menus (
    price_beer float NOT NULL,
    FOREIGN KEY (name_beer) REFERENCES beers(name_beer)
    FOREIGN KEY (name_pub) REFERENCES pubs(name_pub)
);

INSERT INTO beers(name_beer, type_beer)
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

INSERT INTO pubs(name_pub, adress_pub, city_pub)
VALUES 
    ("L'upper", '7 allée Rallier du Baty', 'Rennes'), 
    ("O'Connell's", '7 Place du Parlement de Bretagne', 'Rennes'),
    ("La maison - bar à bières artisanales", '18 rue de Robien', 'Rennes');

INSERT INTO menus(name_pub, name_beer, price_beer)
VALUES 
    ("L'upper", 'Stella Artois', 2.50),
    ("L'upper", 'Corona', 2.50), 
    ("L'upper", 'Carlsberg', 7.00),
    ("L'upper", 'Guinness', 5.43), 
    ("L'upper", 'Kronenbourg', 2.50), 
    ("L'upper", 'Desperados', 4.75),
    ("L'upper", 'Desperados Red', 6.00),
    ("L'upper", 'Hoegaarden', 11.50), 
    ("L'upper", 'Heineken', 7.00), 
    ("L'upper", '1664', 11.50),
    ("L'upper", '1664 Blanche', 5.43),
    ("L'upper", 'Leffe', 4.75), 
    ("L'upper", 'Leffe Ruby', 6.00),
    ("O'Connell's", 'Stella Artois', 5.43),
    ("O'Connell's", 'Corona', 7.00), 
    ("O'Connell's", 'Carlsberg', 2.50),
    ("O'Connell's", 'Guinness', 4.75), 
    ("O'Connell's", 'Kronenbourg', 7.00), 
    ("O'Connell's", 'Desperados', 11.50),
    ("O'Connell's", 'Desperados Red', 11.50),
    ("O'Connell's", 'Hoegaarden', 6.00), 
    ("O'Connell's", 'Heineken', 7.00), 
    ("O'Connell's", '1664', 2.50),
    ("O'Connell's", '1664 Blanche', 5.43),
    ("O'Connell's", 'Leffe', 4.75), 
    ("O'Connell's", 'Leffe Ruby', 6.00),
    ("La maison - bar à bières artisanales", 'Stella Artois', 6.00),
    ("La maison - bar à bières artisanales", 'Corona', 5.43), 
    ("La maison - bar à bières artisanales", 'Carlsberg', 7.00),
    ("La maison - bar à bières artisanales", 'Guinness', 11.50), 
    ("La maison - bar à bières artisanales", 'Kronenbourg', 6.00), 
    ("La maison - bar à bières artisanales", 'Desperados', 7.00),
    ("La maison - bar à bières artisanales", 'Desperados Red', , 2.50),
    ("La maison - bar à bières artisanales", 'Hoegaarden', 5.43), 
    ("La maison - bar à bières artisanales", 'Heineken', 6.00), 
    ("La maison - bar à bières artisanales", '1664', , 2.50),
    ("La maison - bar à bières artisanales", '1664 Blanche', 11.50),
    ("La maison - bar à bières artisanales", 'Leffe', 5.43), 
    ("La maison - bar à bières artisanales", 'Leffe Ruby', 11.50);
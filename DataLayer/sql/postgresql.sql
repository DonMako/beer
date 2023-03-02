DROP TABLE IF EXISTS users;
CREATE TABLE IF NOT EXISTS users (
    id_user CHAR(128) PRIMARY KEY NOT NULL,
    email_user CHAR(128) NOT NULL,
    password_user CHAR(128) NOT NULL,
    favorite_beer_type CHAR(128) NOT NULL,
    favorite_beer_name CHAR(128) NOT NULL,
    budget_user float NOT NULL
);

DROP TABLE IF EXISTS beers;
CREATE TABLE IF NOT EXISTS beers (
    name_beer VARCHAR(50) PRIMARY KEY NOT NULL,
    type_beer CHAR(128) NOT NULL
);

DROP TABLE IF EXISTS pubs;
CREATE TABLE IF NOT EXISTS pubs (
    name_pub VARCHAR(50) PRIMARY KEY NOT NULL,
    adress_pub VARCHAR(50) NOT NULL,
    city_pub CHAR(128) NOT NULL
);

DROP TABLE IF EXISTS menu;
CREATE TABLE IF NOT EXISTS menu (
    id_menu serial PRIMARY KEY NOT NULL,
    price_beer float NOT NULL,
    name_beer VARCHAR(50) NOT NULL, 
    name_pub VARCHAR(50) NOT NULL,
    FOREIGN KEY (name_beer) REFERENCES beers(name_beer),
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
    ('Heineken', 'Blonde'), 
    ('1664', 'Blonde'),
    ('1664 Blanche', 'Blanche'),
    ('Leffe', 'Blonde'), 
    ('Leffe Ruby', 'Rouge');

INSERT INTO pubs(name_pub, adress_pub, city_pub)
VALUES 
    ('Lupper', '7 allée Rallier du Baty', 'Rennes'), 
    ('OConnells', '7 Place du Parlement de Bretagne', 'Rennes'),
    ('La maison - bar à bières artisanales', '18 rue de Robien', 'Rennes');

INSERT INTO menu(name_pub, name_beer, price_beer)
VALUES 
    ('Lupper', 'Stella Artois', 2.50),
    ('Lupper', 'Corona', 2.50), 
    ('Lupper', 'Carlsberg', 7.00),
    ('Lupper', 'Guinness', 5.43), 
    ('Lupper', 'Kronenbourg', 2.50), 
    ('Lupper', 'Desperados', 4.75),
    ('Lupper', 'Desperados Red', 6.00),
    ('Lupper', 'Hoegaarden', 11.50), 
    ('Lupper', 'Heineken', 7.00), 
    ('Lupper', '1664', 11.50),
    ('Lupper', '1664 Blanche', 5.43),
    ('Lupper', 'Leffe', 4.75), 
    ('Lupper', 'Leffe Ruby', 6.00),
    ('OConnells', 'Stella Artois', 5.43),
    ('OConnells', 'Corona', 7.00), 
    ('OConnells', 'Carlsberg', 2.50),
    ('OConnells', 'Guinness', 4.75), 
    ('OConnells', 'Kronenbourg', 7.00), 
    ('OConnells', 'Desperados', 11.50),
    ('OConnells', 'Desperados Red', 11.50),
    ('OConnells', 'Hoegaarden', 6.00), 
    ('OConnells', 'Heineken', 7.00), 
    ('OConnells', '1664', 2.50),
    ('OConnells', '1664 Blanche', 5.43),
    ('OConnells', 'Leffe', 4.75), 
    ('OConnells', 'Leffe Ruby', 6.00),
    ('La maison - bar à bières artisanales', 'Stella Artois', 6.00),
    ('La maison - bar à bières artisanales', 'Corona', 5.43), 
    ('La maison - bar à bières artisanales', 'Carlsberg', 7.00),
    ('La maison - bar à bières artisanales', 'Guinness', 11.50), 
    ('La maison - bar à bières artisanales', 'Kronenbourg', 6.00), 
    ('La maison - bar à bières artisanales', 'Desperados', 7.00),
    ('La maison - bar à bières artisanales', 'Desperados Red', 2.50),
    ('La maison - bar à bières artisanales', 'Hoegaarden', 5.43), 
    ('La maison - bar à bières artisanales', 'Heineken', 6.00), 
    ('La maison - bar à bières artisanales', '1664', 2.50),
    ('La maison - bar à bières artisanales', '1664 Blanche', 11.50),
    ('La maison - bar à bières artisanales', 'Leffe', 5.43), 
    ('La maison - bar à bières artisanales', 'Leffe Ruby', 11.50);

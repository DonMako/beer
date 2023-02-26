DROP TABLE IF EXISTS users;
CREATE TABLE IF NOT EXISTS users (
    id_user CHAR(128) NOT NULL,
    password_user CHAR(128) NOT NULL,
    favorite_type_beer CHAR(128) NOT NULL,
    budget_user float8 NOT NULL,
);

DROP TABLE IF EXISTS beers;
CREATE TABLE IF NOT EXISTS beers (
    name_beer VARCHAR(50) NOT NULL,
    type_beer CHAR(128) NOT NULL,
    price_beer float8 NOT NULL,
);

DROP TABLE IF EXISTS pubs;
CREATE TABLE IF NOT EXISTS pubs (
    name_pub VARCHAR(50) NOT NULL,
    localisation_pub VARCHAR(50) NOT NULL,
);
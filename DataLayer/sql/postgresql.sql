DROP TABLE IF EXISTS users;
CREATE TABLE IF NOT EXISTS users (
    surname VARCHAR(50) NOT NULL,
    name_user VARCHAR(100) NOT NULL
    id_user SERIAL PRIMARY KEY,
    password_user CHAR(128) NOT NULL,
    favorite_type_beer float8 NOT NULL,
);

DROP TABLE IF EXISTS beers;
CREATE TABLE IF NOT EXISTS beers (
    name_beer VARCHAR(50) NOT NULL,
    price,
);

DROP TABLE IF EXISTS bars;
CREATE TABLE IF NOT EXISTS bars (
    name_bar VARCHAR(50) NOT NULL,
    localisation,
);

INSERT INTO modeles (nom_modele, regex_nom_fichier, position_champ_numero,
                     position_champ_voie, position_champ_code_postal, position_champ_ville)
VALUES ('Modèle par défaut','.*','{0}','{1}','{2}','{3}');
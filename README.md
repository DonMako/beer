# Projet BIERE

## Qu'est-ce que le projet BIERE ?

Le projet BIERE, pour "Bacchus : Identification Et Récupération des Établissements", vise à donner des adresses de bars à ses utilisateurs, selon leur localisation et leur profil (péférence en matière de type de bière et budget).

## Comment ça marche ?

Le projet BIERE est une application dans laquelle l'utilisateur renseigne le lieu où il se trouve. 
L'application requête ensuite l'API Places de Google Maps afin de trouver les lieux.

## Structure des données

```mermaid
classDiagram
    Beer <|-- User
    Bar <|-- Beer
    class User{
      +String identifier
      +String password
      +String favoriteBeerType
    }
    class Beer{
      +String name_beer
      +String type
      +String price
    }
    class Bar{
      +String name_bar
      +String localisation
    }
```

## Auteurs

BERTAIL Aurélien
ÉVAIN Manon
MACAUX Lucas

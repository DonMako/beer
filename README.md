# Project BIERE

## What is the BIERE project ?

The BIERE project (for "Bacchus : Identification Et Récupération des Établissements") is a french application aiming to give pubs' adresses to users, according to their localisation and their profile (the favorite beer flavor and their budget).

## Installation

### Via l'interpréteur Python

If you have Python 3 and pip installed on your system, you can install and execute the BIERE project from its sources:

```
git clone https://github.com/DonMako/beer.git
cd beer
pip install -r requirements.txt
python main.py
```

## How does it work ?

The user of the BIERE project must connect to his account or create one.
The user can then access all the features allowed by the application:
- change information on his/her account or delete it;
- use the main deature of the application: the localisation of pubs.

### If the user chooses to use the main feature of the application :

The user must indicate his/her localisation. The application searches then in its database the name of pubs that
- are located in the localisation indicated by the user in his/er profile;
- are selling beers from the favorite beer type of the user and in his/her budget.
The application displays finally the name of the corresponding pubs.

## Data structure

```mermaid
classDiagram
    Bar <|-- Beer
    class User{
      +String id
      +String password
      +String favoriteBeerType
      +Float budget
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

## Ideas for the future

Here are some ideas that we want to implement to increase the utility of the project BIERE :
- make phone version of the application (IOS & Android);
- use Google Maps' API Places instead of a fixed database of pubs, so that the data would be up-to-date.

## Authors

BERTAIL Aurélien

ÉVAIN Manon

MACAUX Lucas
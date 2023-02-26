class User(object):
    id: str
    password: str
    favorite_beer_flavor: str
    budget: float

    def as_dict(self) -> dict:
        data = {"id": self.id, "password": self.password, "favorite_beer_flavor": self.favorite_beer_flavor, "budget": self.budget}
        return
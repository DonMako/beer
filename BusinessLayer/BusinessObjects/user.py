class User(object):
    id_user: str
    email_user: str
    password_user: str
    favorite_beer_flavor: str
    budget_user: float

    def as_dict(self) -> dict:
        data = {"id_user": self.id_user, "email_user": self.email_user, "password_user": self.password_user,
                "favorite_beer_flavor": self.favorite_beer_flavor, "budget_user": self.budget_user}
        return data
    
    @staticmethod
    def from_dict(data: dict):
        user = User(data["id_user"], data["email_user"], data["password_user"], data["favorite_beer_flavor"], data["budget_user"])
        return user
import attr


@attr.s
class User(object):

    id_user: str = attr.ib(converter=str, on_setattr=attr.setters.convert)
    email_user: str = attr.ib(converter=str, on_setattr=attr.setters.convert)
    password_user: str = attr.ib(converter=str, on_setattr=attr.setters.convert)
    favorite_beer_type: str = attr.ib(converter=str, on_setattr=attr.setters.convert)
    favorite_beer_name: str = attr.ib(converter=str, on_setattr=attr.setters.convert)
    budget_user: float = attr.ib(converter=float, on_setattr=attr.setters.convert)

    def as_dict(self) -> dict:
        data = {"id_user": self.id_user, "email_user": self.email_user, "password_user": self.password_user,
                "favorite_beer_type": self.favorite_beer_type, "favorite_beer_name": self.favorite_beer_name, "budget_user": self.budget_user}
        return data
    
    @staticmethod
    def from_dict(data: dict):
        user = User(data["id_user"], data["email_user"], data["password_user"], data["favorite_beer_type"], data["favorite_beer_name"], data["budget_user"])
        return user
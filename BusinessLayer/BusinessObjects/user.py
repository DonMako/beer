import attr


@attr.s
class User(object):

    id_user: str = attr.ib(converter=str, on_setattr=attr.setters.convert)
    email_user: str = attr.ib(converter=str, on_setattr=attr.setters.convert)
    password_user: str = attr.ib(converter=str, on_setattr=attr.setters.convert)
    favorite_beer_flavor: str = attr.ib(converter=str, on_setattr=attr.setters.convert)
    budget_user: float = attr.ib(converter=float, on_setattr=attr.setters.convert)

    def as_dict(self) -> dict:
        data = {"id_user": self.id_user, "email_user": self.email_user, "password_user": self.password_user,
                "favorite_beer_flavor": self.favorite_beer_flavor, "budget_user": self.budget_user}
        return data
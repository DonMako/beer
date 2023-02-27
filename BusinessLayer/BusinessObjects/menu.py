import attr


@attr.s
class Menu(object):

    name_pub: str = attr.ib(converter=str, on_setattr=attr.setters.convert)
    name_beer: str = attr.ib(converter=str, on_setattr=attr.setters.convert)
    price_beer: float = attr.ib(converter=float, on_setattr=attr.setters.convert)

    def as_dict(self) -> dict:
        data = {"name_pub": self.name_pub, "name_beer": self.name_beer, "price_beer": self.price_beer}
        return data
    
    @staticmethod
    def from_dict(data: dict):
        user = Menu(data["name_pub"], data["name_beer"], data["price_beer"])
        return user
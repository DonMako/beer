import attr


@attr.s
class Pub(object):

    name_pub: str = attr.ib(converter=str, on_setattr=attr.setters.convert)
    adress_pub: str = attr.ib(converter=str, on_setattr=attr.setters.convert)
    city_pub: str = attr.ib(converter=str, on_setattr=attr.setters.convert)

    def as_dict(self) -> dict:
        data = {"name_pub": self.name_pub, "adress_pub": self.adress_pub, "city_pub": self.city_pub}
        return data
    
    @staticmethod
    def from_dict(data: dict):
        user = Pub(data["name_pub"], data["adress_pub"], data["city_pub"])
        return user
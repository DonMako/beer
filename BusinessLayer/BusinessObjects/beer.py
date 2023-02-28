import attr


@attr.s
class Beer(object):

    name_beer: str = attr.ib(converter=str, on_setattr=attr.setters.convert)
    type_beer: str = attr.ib(converter=str, on_setattr=attr.setters.convert)

    def as_dict(self) -> dict:
        data = {"name_beer": self.name_beer, "type_beer": self.type_beer}
        return data
    
    @staticmethod
    def from_dict(data: dict):
        user = Beer(data["name_beer"], data["type_beer"])
        return user
import attr


@attr.s
class Pub(object):

    name_pub: str = attr.ib(converter=str, on_setattr=attr.setters.convert)
    localisation_pub: str = attr.ib(converter=str, on_setattr=attr.setters.convert)
    menu_bar: dict = attr.ib(converter=dict, on_setattr=attr.setters.convert)

    def as_dict(self) -> dict:
        data = {"name_pub": self.name_pub, "localisation_pub": self.localisation_pub, "menu_bar": self.menu_bar}
        return data
    
    @staticmethod
    def from_dict(data: dict):
        user = Pub(data["name_pub"], data["localisation_pub"], data["menu_bar"])
        return user
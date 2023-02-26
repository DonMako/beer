import attr


@attr.s
class Beer(object):
    prenom: str = attr.ib(converter=str, on_setattr=attr.setters.convert)
    nom: str = attr.ib(converter=str, on_setattr=attr.setters.convert)
    quotite: float = attr.ib(converter=float, on_setattr=attr.setters.convert)
    agent_id: int = attr.ib(default=None, converter=attr.converters.optional(int), on_setattr=attr.setters.frozen)

    def as_dict(self) -> dict:
        data = {"identifiant_agent": self.agent_id, "quotite": self.quotite, "prenom": self.prenom, "nom": self.nom}
        return
from collections import namedtuple

RessourceData = namedtuple("RessourceData", ["filename", "score", "last_seen_date"])


class RessourcePicker:
    def __init__(self, ressources: list[RessourceData]) -> None:
        self._data = ressources
        self._waiting_result = False

        """
        self._data = sorted(
            ressources, key=lambda ressourceData: ressourceData.score
        )
        """

    def pick(self) -> str:
        """
        Returns a ressource name
        """
        if self._waiting_result:
            msg = "Can't pick result, need to set_result() before"
            raise RuntimeError(msg)

        self._waiting_result = True

        for ressource in self._data:
            return ressource.filename

    def set_result(self, success: bool) -> None:
        if not self._waiting_result:
            msg = "Can't set result, need to pick() before"
            raise RuntimeError(msg)

        self._waiting_result = False

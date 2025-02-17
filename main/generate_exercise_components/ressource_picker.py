import datetime
from collections import namedtuple

RessourceData = namedtuple("RessourceData", ["filename", "score", "last_seen_date"])


class RessourcePicker:
    def __init__(self, ressources: list[RessourceData]) -> None:
        self.ressources = ressources
        self._waiting_result = False

    def pick(self) -> str | None:
        """
        Returns a ressource name
        """
        self._sort_ressources()

        if self._waiting_result:
            msg = "Could not pick result, need to set_result before"
            raise RuntimeError(msg)

        self._waiting_result = True

        today = datetime.datetime.now().date()
        self._picked_index = -1

        for index, ressource in enumerate(self.ressources):
            if ressource.last_seen_date != today:
                self._picked_index = index
                return ressource.filename

        return None

    def set_result(self, success: bool) -> None:
        if not self._waiting_result:
            msg = "Could not set result, need to pick before"
            raise RuntimeError(msg)

        self._waiting_result = False

        new_score = self.ressources[self._picked_index].score
        if success:
            new_score += min(new_score * -0.29 + 30, 100)
        else:
            new_score /= 2

        print(
            f"Score update on {self.ressources[self._picked_index].filename}: "
            f"{self.ressources[self._picked_index].score} -> {new_score}"
        )
        self.ressources[self._picked_index] = RessourceData(
            filename=self.ressources[self._picked_index].filename,
            score=new_score,
            last_seen_date=datetime.datetime.now().date(),
        )

    def _sort_ressources(self):
        self.ressources = sorted(
            self.ressources, key=lambda ressourceData: ressourceData.score
        )

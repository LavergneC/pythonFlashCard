import datetime
from collections import namedtuple

ResourceData = namedtuple("ResourceData", ["filename", "score", "last_seen_date"])


class ResourcePicker:
    def __init__(self, resources: list[ResourceData]) -> None:
        self.resources = resources
        self._waiting_result = False

    def pick(self) -> str | None:
        """
        Returns a resource name
        """
        self._sort_resources()

        if self._waiting_result:
            msg = "Could not pick result, need to set_result before"
            raise RuntimeError(msg)

        self._waiting_result = True

        today = datetime.datetime.now().date()
        self._picked_index = -1

        for index, resource in enumerate(self.resources):
            if resource.last_seen_date != today:
                self._picked_index = index
                return resource.filename

        return None

    def set_result(self, success: bool) -> None:
        if not self._waiting_result:
            msg = "Could not set result, need to pick before"
            raise RuntimeError(msg)

        self._waiting_result = False

        new_score = self.resources[self._picked_index].score
        if success:
            new_score += min(new_score * -0.29 + 30, 100)
        else:
            new_score /= 2

        print(
            f"Score update on {self.resources[self._picked_index].filename}: "
            f"{int(self.resources[self._picked_index].score)}% -> {int(new_score)}%"
        )
        self.resources[self._picked_index] = ResourceData(
            filename=self.resources[self._picked_index].filename,
            score=new_score,
            last_seen_date=datetime.datetime.now().date(),
        )

    def _sort_resources(self):
        self.resources = sorted(
            self.resources, key=lambda resourceData: resourceData.score
        )

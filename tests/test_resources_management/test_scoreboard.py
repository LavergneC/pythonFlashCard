import datetime

import pytest

from main.resources_management.resource_picker import ResourceData
from main.resources_management.scoreboard import Scoreboard


class TestScoreboard:
    @pytest.fixture
    def resources(self) -> list[ResourceData]:
        now = datetime.datetime.now()
        return [
            ResourceData(filename="Resource 1", score=100, last_seen_date=now),
            ResourceData(filename="Resource 2", score=100, last_seen_date=now),
            ResourceData(filename="Resource 3", score=2, last_seen_date=now),
            ResourceData(filename="Resource 4", score=1.127, last_seen_date=now),
            ResourceData(filename="Resource 5", score=20, last_seen_date=now),
            ResourceData(filename="Resource 6", score=95, last_seen_date=now),
        ]

    def test_get_worse_resources(self, resources: list[ResourceData]):
        assert Scoreboard._worse_resources(resources) == [
            ("Resource 4", 1.127),
            ("Resource 3", 2),
            ("Resource 5", 20),
        ]

    def test_display_scoreboard(self, resources: list[ResourceData]):
        assert (
            Scoreboard.scoreboard(resources)
            == "Your current score is 1.13. Because of:\n"
            "\t-'Resource 4'\t1.13 points\n"
            "\t-'Resource 3'\t2 points\n"
            "\t-'Resource 5'\t20 points"
        )

    def test_display_short_version(self, resources: list[ResourceData]):
        assert Scoreboard.score(resources) == "Your current score is 1.13"

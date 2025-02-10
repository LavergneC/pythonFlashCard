import datetime
import shutil

from main.ressource_picker import RessourceData
from main.ressource_storage import RessouceStorage
from tests.constants_test import TEST_RESSOURCE_STORAGE


def test_get_ressrouce_from_csv() -> None:
    shutil.copyfile(TEST_RESSOURCE_STORAGE.PATH, TEST_RESSOURCE_STORAGE.PATH_COPY)
    rs = RessouceStorage(TEST_RESSOURCE_STORAGE.PATH_COPY)

    ressources = rs.read()
    assert len(ressources) == 3
    assert ressources[0].filename == "test_ressource_1.py"
    assert ressources[0].score == 5
    assert ressources[0].last_seen_date == datetime.date(year=2025, month=1, day=15)

    assert ressources[1].filename == "test_ressource_2.py"
    assert ressources[1].score == 88
    assert ressources[1].last_seen_date == datetime.date(year=2024, month=5, day=23)

    assert ressources[2].filename == "test_ressource_3.py"
    assert ressources[2].score == 15
    assert ressources[2].last_seen_date == datetime.date(year=2000, month=12, day=30)


def test_set_ressource() -> None:
    shutil.copyfile(TEST_RESSOURCE_STORAGE.PATH, TEST_RESSOURCE_STORAGE.PATH_COPY)

    rs = RessouceStorage(ressource_csv_path=TEST_RESSOURCE_STORAGE.PATH_COPY)
    ressources = rs.read()

    assert ressources[0].score != 123
    assert ressources[0].last_seen_date != datetime.date(year=2015, month=5, day=15)

    ressources[0] = RessourceData(
        filename=ressources[0].filename,
        score=123,
        last_seen_date=datetime.date(year=2015, month=5, day=15),
    )
    rs.write(ressources=ressources)

    rs = RessouceStorage(ressource_csv_path=TEST_RESSOURCE_STORAGE.PATH_COPY)
    ressources = rs.read()
    assert ressources[0].score == 123
    assert ressources[0].last_seen_date == datetime.date(year=2015, month=5, day=15)

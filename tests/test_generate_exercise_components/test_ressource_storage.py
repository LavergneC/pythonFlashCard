import datetime
import os
import shutil

from main.generate_exercise_components.ressource_picker import RessourceData
from main.generate_exercise_components.ressource_storage import RessouceStorage
from tests.constants_test import TEST_RESSOURCE_STORAGE, TEST_RESSOURCE_STORAGE_CSV


def test_get_ressrouce_from_csv() -> None:
    shutil.copyfile(
        TEST_RESSOURCE_STORAGE_CSV.PATH, TEST_RESSOURCE_STORAGE_CSV.PATH_COPY
    )
    rs = RessouceStorage(
        ressource_csv_path=TEST_RESSOURCE_STORAGE_CSV.PATH_COPY,
        ressource_directory_path="",
    )

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
    shutil.copyfile(
        TEST_RESSOURCE_STORAGE_CSV.PATH, TEST_RESSOURCE_STORAGE_CSV.PATH_COPY
    )

    rs = RessouceStorage(
        ressource_csv_path=TEST_RESSOURCE_STORAGE_CSV.PATH_COPY,
        ressource_directory_path="",
    )
    ressources = rs.read()

    assert ressources[0].score != 123
    assert ressources[0].last_seen_date != datetime.date(year=2015, month=5, day=15)

    ressources[0] = RessourceData(
        filename=ressources[0].filename,
        score=123,
        last_seen_date=datetime.date(year=2015, month=5, day=15),
    )
    rs.write(ressources=ressources)

    rs = RessouceStorage(
        ressource_csv_path=TEST_RESSOURCE_STORAGE_CSV.PATH_COPY,
        ressource_directory_path="",
    )
    ressources = rs.read()
    assert ressources[0].score == 123
    assert ressources[0].last_seen_date == datetime.date(year=2015, month=5, day=15)


def test_db_initialization() -> None:
    # Make sure there is no db
    if os.path.exists(TEST_RESSOURCE_STORAGE_CSV.PATH_NEW_DB):
        os.remove(TEST_RESSOURCE_STORAGE_CSV.PATH_NEW_DB)

    rs = RessouceStorage(
        ressource_csv_path=TEST_RESSOURCE_STORAGE_CSV.PATH_NEW_DB,
        ressource_directory_path=TEST_RESSOURCE_STORAGE.PATH,
    )
    ressources = rs.read()

    yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).date()

    assert ressources == [
        RessourceData(filename="ressource2.py", score=0, last_seen_date=yesterday),
        RessourceData(filename="ressource1.py", score=0, last_seen_date=yesterday),
    ]
    assert os.path.exists(TEST_RESSOURCE_STORAGE_CSV.PATH_COPY)

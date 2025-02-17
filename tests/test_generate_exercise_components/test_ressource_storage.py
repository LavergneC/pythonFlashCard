import datetime
import os
import shutil

import pytest

from main.generate_exercise_components.ressource_picker import RessourceData
from main.generate_exercise_components.ressource_storage import RessouceStorage
from tests.constants_test import TEST_RESSOURCE_STORAGE


@pytest.fixture
def csv_db_file():
    shutil.copyfile(TEST_RESSOURCE_STORAGE.DB_PATH, TEST_RESSOURCE_STORAGE.DB_PATH_COPY)
    yield TEST_RESSOURCE_STORAGE.DB_PATH_COPY

    # tear down
    os.remove(TEST_RESSOURCE_STORAGE.DB_PATH_COPY)


def test_get_ressource_from_csv(csv_db_file) -> None:
    rs = RessouceStorage(
        ressource_csv_path=csv_db_file,
        ressource_directory_path=TEST_RESSOURCE_STORAGE.PATH,
    )

    ressources = rs.read()
    assert len(ressources) == 2
    assert ressources[0].filename == "test_ressource_10.py"
    assert ressources[0].score == 5
    assert ressources[0].last_seen_date == datetime.date(year=2025, month=1, day=15)

    assert ressources[1].filename == "test_ressource_20.py"
    assert ressources[1].score == 88
    assert ressources[1].last_seen_date == datetime.date(year=2024, month=5, day=23)


def test_set_ressource(csv_db_file) -> None:
    rs = RessouceStorage(
        ressource_csv_path=TEST_RESSOURCE_STORAGE.DB_PATH_COPY,
        ressource_directory_path=TEST_RESSOURCE_STORAGE.PATH,
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
        ressource_csv_path=TEST_RESSOURCE_STORAGE.DB_PATH_COPY,
        ressource_directory_path=TEST_RESSOURCE_STORAGE.PATH,
    )
    ressources = rs.read()
    assert ressources[0].score == 123
    assert ressources[0].last_seen_date == datetime.date(year=2015, month=5, day=15)


def test_db_initialization() -> None:
    # Make sure there is no db
    if os.path.exists(TEST_RESSOURCE_STORAGE.db_PATH_NEW_DB):
        os.remove(TEST_RESSOURCE_STORAGE.db_PATH_NEW_DB)

    rs = RessouceStorage(
        ressource_csv_path=TEST_RESSOURCE_STORAGE.db_PATH_NEW_DB,
        ressource_directory_path=TEST_RESSOURCE_STORAGE.PATH,
    )

    ressources = rs.read()
    yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).date()

    assert (
        RessourceData(
            filename=TEST_RESSOURCE_STORAGE.RESSOURCE_1,
            score=0,
            last_seen_date=yesterday,
        )
        in ressources
    )

    assert (
        RessourceData(
            filename=TEST_RESSOURCE_STORAGE.RESSOURCE_2,
            score=0,
            last_seen_date=yesterday,
        )
        in ressources
    )

    assert len(ressources) == 2
    assert os.path.exists(TEST_RESSOURCE_STORAGE.db_PATH_NEW_DB)


@pytest.fixture
def third_ressource():
    shutil.copyfile(
        TEST_RESSOURCE_STORAGE.RESSOURCE_3_FROM, TEST_RESSOURCE_STORAGE.RESSOURCE_3_TO
    )
    yield TEST_RESSOURCE_STORAGE.RESSOURCE_3

    # Teardown
    os.remove(TEST_RESSOURCE_STORAGE.RESSOURCE_3_TO)


def test_adding_a_new_ressource(csv_db_file, third_ressource) -> None:
    rs = RessouceStorage(
        ressource_csv_path=csv_db_file,
        ressource_directory_path=TEST_RESSOURCE_STORAGE.PATH,
    )

    ressources = rs.read()
    yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).date()

    assert (
        RessourceData(
            filename=third_ressource,
            score=0,
            last_seen_date=yesterday,
        )
        in ressources
    )

    assert len(ressources) == 3

    # TODO make the test_db.csv match the dir content

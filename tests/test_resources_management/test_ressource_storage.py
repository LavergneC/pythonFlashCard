import datetime
import os
import shutil

import pytest

from main.resources_management.resource_picker import ResourceData
from main.resources_management.resource_storage import ResourceStorage
from tests.constants_test import TEST_RESOURCE_STORAGE


@pytest.fixture
def csv_db_file():
    shutil.copyfile(TEST_RESOURCE_STORAGE.DB_PATH, TEST_RESOURCE_STORAGE.DB_PATH_COPY)
    yield TEST_RESOURCE_STORAGE.DB_PATH_COPY

    # tear down
    os.remove(TEST_RESOURCE_STORAGE.DB_PATH_COPY)


@pytest.fixture
def empty_db_file():
    if os.path.exists(TEST_RESOURCE_STORAGE.EMPTY_DB_PATH):
        os.remove(TEST_RESOURCE_STORAGE.EMPTY_DB_PATH)

    yield TEST_RESOURCE_STORAGE.EMPTY_DB_PATH

    os.remove(TEST_RESOURCE_STORAGE.EMPTY_DB_PATH)


def test_get_resource_from_csv(csv_db_file) -> None:
    rs = ResourceStorage(
        resource_csv_path=csv_db_file,
        resource_directory_path=TEST_RESOURCE_STORAGE.PATH,
    )

    resources = rs.read()
    assert len(resources) == 2
    assert resources[0].filename == "test_resource_10.py"
    assert resources[0].score == 5
    assert resources[0].last_seen_date == datetime.date(year=2025, month=1, day=15)

    assert resources[1].filename == "test_dir/test_resource_20.py"
    assert resources[1].score == 88
    assert resources[1].last_seen_date == datetime.date(year=2024, month=5, day=23)


def test_set_resource(csv_db_file) -> None:
    rs = ResourceStorage(
        resource_csv_path=TEST_RESOURCE_STORAGE.DB_PATH_COPY,
        resource_directory_path=TEST_RESOURCE_STORAGE.PATH,
    )
    resources = rs.read()

    assert resources[0].score != 123
    assert resources[0].last_seen_date != datetime.date(year=2015, month=5, day=15)

    resources[0] = ResourceData(
        filename=resources[0].filename,
        score=123,
        last_seen_date=datetime.date(year=2015, month=5, day=15),
    )
    rs.write(resources=resources)

    rs = ResourceStorage(
        resource_csv_path=TEST_RESOURCE_STORAGE.DB_PATH_COPY,
        resource_directory_path=TEST_RESOURCE_STORAGE.PATH,
    )
    resources = rs.read()
    assert resources[0].score == 123
    assert resources[0].last_seen_date == datetime.date(year=2015, month=5, day=15)


def test_db_initialization_from_files() -> None:
    # Make sure there is no db
    if os.path.exists(TEST_RESOURCE_STORAGE.db_PATH_NEW_DB):
        os.remove(TEST_RESOURCE_STORAGE.db_PATH_NEW_DB)

    rs = ResourceStorage(
        resource_csv_path=TEST_RESOURCE_STORAGE.db_PATH_NEW_DB,
        resource_directory_path=TEST_RESOURCE_STORAGE.PATH,
    )

    resources = rs.read()
    yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).date()

    assert (
        ResourceData(
            filename=TEST_RESOURCE_STORAGE.RESOURCE_1,
            score=0,
            last_seen_date=yesterday,
        )
        in resources
    )

    assert (
        ResourceData(
            filename=TEST_RESOURCE_STORAGE.RESOURCE_2,
            score=0,
            last_seen_date=yesterday,
        )
        in resources
    )

    assert len(resources) == 2
    assert os.path.exists(TEST_RESOURCE_STORAGE.db_PATH_NEW_DB)


def test_db_initialization_from_files_for_quiz() -> None:
    # Make sure there is no db
    if os.path.exists(TEST_RESOURCE_STORAGE.db_PATH_NEW_DB):
        os.remove(TEST_RESOURCE_STORAGE.db_PATH_NEW_DB)

    rs = ResourceStorage(
        resource_csv_path=TEST_RESOURCE_STORAGE.db_PATH_NEW_DB,
        resource_directory_path=TEST_RESOURCE_STORAGE.PATH_QUIZ,
    )
    resources = rs.read()

    yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).date()

    assert (
        ResourceData(
            filename=TEST_RESOURCE_STORAGE.RESOURCE_4,
            score=0,
            last_seen_date=yesterday,
        )
        in resources
    )
    assert len(resources) == 1


@pytest.fixture
def third_resource():
    shutil.copyfile(
        TEST_RESOURCE_STORAGE.RESOURCE_3_FROM, TEST_RESOURCE_STORAGE.RESOURCE_3_TO
    )
    yield TEST_RESOURCE_STORAGE.RESOURCE_3

    # Teardown
    os.remove(TEST_RESOURCE_STORAGE.RESOURCE_3_TO)


def test_adding_a_new_resource(csv_db_file, third_resource) -> None:
    rs = ResourceStorage(
        resource_csv_path=csv_db_file,
        resource_directory_path=TEST_RESOURCE_STORAGE.PATH,
    )

    resources = rs.read()
    yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).date()

    assert (
        ResourceData(
            filename=third_resource,
            score=0,
            last_seen_date=yesterday,
        )
        in resources
    )

    assert len(resources) == 3

    # TODO make the test_db.csv match the dir content


def test_get_resource_filenames(empty_db_file):
    rs = ResourceStorage(
        resource_csv_path=empty_db_file,
        resource_directory_path=TEST_RESOURCE_STORAGE.PATH,
    )

    resources_paths = [data.filename for data in rs.read()]

    assert "test_resource_10.py" in resources_paths
    assert "test_dir/test_resource_20.py" in resources_paths
    assert len(resources_paths) == 2

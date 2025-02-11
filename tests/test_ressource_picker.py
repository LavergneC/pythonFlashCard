import datetime

import pytest

from main.generate_exercise_components.ressource_picker import (
    RessourceData,
    RessourcePicker,
)


def _change_all_dates(ressource_picker) -> None:
    """
    Any ressouce can be picked only once a day, for test purpose we need to
    change all dates in order to hide this feature.
    """
    new_date = datetime.date(year=2000, month=2, day=15)
    for ressource_index, ressourceData in enumerate(ressource_picker._data):
        new_data = RessourceData(
            filename=ressourceData.filename,
            score=ressourceData.score,
            last_seen_date=new_date,
        )
        ressource_picker._data[ressource_index] = new_data


def _set_success_and_change_date(ressource_picker):
    ressource_picker.set_result(success=True)
    _change_all_dates(ressource_picker)


def _get_default_ressources() -> list[RessourceData]:
    yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).date()
    return [
        RessourceData(filename="Ressource 1", score=0, last_seen_date=yesterday),
        RessourceData(filename="Ressource 2", score=1, last_seen_date=yesterday),
        RessourceData(filename="Ressource 3", score=2, last_seen_date=yesterday),
    ]


def test_success_cycle():
    ressource_picker = RessourcePicker(_get_default_ressources())

    assert ressource_picker.pick() == "Ressource 1"
    _set_success_and_change_date(ressource_picker)

    assert ressource_picker.pick() == "Ressource 2"
    _set_success_and_change_date(ressource_picker)

    assert ressource_picker.pick() == "Ressource 3"
    _set_success_and_change_date(ressource_picker)

    assert ressource_picker.pick() == "Ressource 1"
    _set_success_and_change_date(ressource_picker)

    assert ressource_picker.pick() == "Ressource 2"
    _set_success_and_change_date(ressource_picker)

    assert ressource_picker.pick() == "Ressource 3"
    _set_success_and_change_date(ressource_picker)

    assert ressource_picker.pick() == "Ressource 1"


def test_user_must_set_result_between_picks():
    ressource_picker = RessourcePicker(_get_default_ressources())

    assert ressource_picker.pick() == "Ressource 1"
    with pytest.raises(
        RuntimeError, match="Could not pick result, need to set_result before"
    ):
        ressource_picker.pick()


def test_user_must_pick_ressource_before_settting_result():
    ressource_picker = RessourcePicker(_get_default_ressources())

    with pytest.raises(RuntimeError, match="Could not set result, need to pick before"):
        ressource_picker.set_result(success=True)

    ressource_picker.pick()
    ressource_picker.set_result(success=True)

    with pytest.raises(RuntimeError, match="Could not set result, need to pick before"):
        ressource_picker.set_result(success=False)


def test_success_and_fails():
    ressource_picker = RessourcePicker(_get_default_ressources())
    assert ressource_picker.pick() == "Ressource 1"
    ressource_picker.set_result(success=True)

    assert ressource_picker.pick() == "Ressource 2"
    ressource_picker.set_result(success=False)

    assert ressource_picker.pick() == "Ressource 3"
    ressource_picker.set_result(success=True)

    _change_all_dates(ressource_picker)
    assert ressource_picker.pick() == "Ressource 2"

import datetime

import pytest

from main.resources_management.resource_picker import (
    ResourceData,
    ResourcePicker,
)


def _change_all_dates(resource_picker: ResourcePicker) -> None:
    """
    Any resource can be picked only once a day, for test purpose we need to
    change all dates in order to hide this feature.
    """
    new_date = datetime.date(year=2000, month=2, day=15)
    for resource_index, resourceData in enumerate(resource_picker.resources):
        new_data = ResourceData(
            filename=resourceData.filename,
            score=resourceData.score,
            last_seen_date=new_date,
        )
        resource_picker.resources[resource_index] = new_data


def _set_success_and_change_date(resource_picker):
    resource_picker.set_result(success=True)
    _change_all_dates(resource_picker)


def _get_default_resources() -> list[ResourceData]:
    yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).date()
    return [
        ResourceData(filename="Resource 1", score=0, last_seen_date=yesterday),
        ResourceData(filename="Resource 2", score=1, last_seen_date=yesterday),
        ResourceData(filename="Resource 3", score=2, last_seen_date=yesterday),
    ]


def test_success_cycle():
    resource_picker = ResourcePicker(_get_default_resources())

    assert resource_picker.pick() == "Resource 1"
    _set_success_and_change_date(resource_picker)

    assert resource_picker.pick() == "Resource 2"
    _set_success_and_change_date(resource_picker)

    assert resource_picker.pick() == "Resource 3"
    _set_success_and_change_date(resource_picker)

    assert resource_picker.pick() == "Resource 1"
    _set_success_and_change_date(resource_picker)

    assert resource_picker.pick() == "Resource 2"
    _set_success_and_change_date(resource_picker)

    assert resource_picker.pick() == "Resource 3"
    _set_success_and_change_date(resource_picker)

    assert resource_picker.pick() == "Resource 1"


def test_user_must_set_result_between_picks():
    resource_picker = ResourcePicker(_get_default_resources())

    assert resource_picker.pick() == "Resource 1"
    with pytest.raises(
        RuntimeError, match="Could not pick result, need to set_result before"
    ):
        resource_picker.pick()


def test_user_must_pick_resource_before_setting_result():
    resource_picker = ResourcePicker(_get_default_resources())

    with pytest.raises(RuntimeError, match="Could not set result, need to pick before"):
        resource_picker.set_result(success=True)

    resource_picker.pick()
    resource_picker.set_result(success=True)

    with pytest.raises(RuntimeError, match="Could not set result, need to pick before"):
        resource_picker.set_result(success=False)


def test_success_and_fails():
    resource_picker = ResourcePicker(_get_default_resources())
    assert resource_picker.pick() == "Resource 1"
    resource_picker.set_result(success=True)

    assert resource_picker.pick() == "Resource 2"
    resource_picker.set_result(success=False)

    assert resource_picker.pick() == "Resource 3"
    resource_picker.set_result(success=True)

    _change_all_dates(resource_picker)
    assert resource_picker.pick() == "Resource 2"

import csv
import os
from datetime import datetime, timedelta

from main.generate_exercise_components.resource_picker import ResourceData


class RESOURCEStorage:
    def __init__(self, resource_csv_path: str, resource_directory_path: str) -> None:
        self.dir_path = resource_directory_path
        self.resource_csv_path = resource_csv_path

        old_db = []
        if os.path.exists(self.resource_csv_path):
            old_db = self.read()

        new_resources = [
            self._get_or_create_resource_data(
                filename=file_name,
                resource_list=old_db,
            )
            for file_name in self._get_resource_filenames()
        ]

        self.write(new_resources)

    def read(self) -> list[ResourceData]:
        with open(self.resource_csv_path, "r") as f:
            reader = csv.DictReader(f)
            return [
                ResourceData(
                    row["filename"],
                    float(row["score"]),
                    datetime.strptime(row["last_seen_date"], "%Y-%m-%d").date(),
                )
                for row in reader
            ]
        return []

    def write(self, resources: list[ResourceData]) -> None:
        with open(self.resource_csv_path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(ResourceData._fields)
            writer.writerows(resources)

    def _get_resource_filenames(self) -> list[str]:
        resource_filenames = []

        for path, _, files in os.walk(self.dir_path):
            resource_filenames += [
                self._get_filepath(path, filename)
                for filename in files
                if filename.endswith(".py")
            ]

        return resource_filenames

    def _get_or_create_resource_data(
        self, filename: str, resource_list: list[ResourceData]
    ) -> ResourceData:
        for resource in resource_list:
            if resource.filename == filename:
                return resource

        yesterday = (datetime.now() - timedelta(days=1)).date()
        return ResourceData(filename=filename, score=0, last_seen_date=yesterday)

    def _get_filepath(self, path: str, filename: str) -> str:
        filepath = path + "/" + filename
        filepath = filepath.replace(self.dir_path, "")
        filepath = filepath.replace("/", "", 1)
        return filepath

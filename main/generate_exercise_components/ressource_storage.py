import csv
import os
from datetime import datetime, timedelta
from os.path import isfile, join

from main.generate_exercise_components.ressource_picker import RessourceData


class RessouceStorage:
    def __init__(self, ressource_csv_path: str, ressource_directory_path: str) -> None:
        self.dir_path = ressource_directory_path
        self.ressource_csv_path = ressource_csv_path

        old_db = []
        if os.path.exists(self.ressource_csv_path):
            old_db = self.read()

        new_ressources = [
            self._create_or_get_ressource_data(
                filename=file_name,
                ressource_list=old_db,
            )
            for file_name in self._get_ressource_filenames()
        ]

        self.write(new_ressources)

    def read(self) -> list[RessourceData]:
        with open(self.ressource_csv_path, "r") as f:
            reader = csv.DictReader(f)
            return [
                RessourceData(
                    row["filename"],
                    float(row["score"]),
                    datetime.strptime(row["last_seen_date"], "%Y-%m-%d").date(),
                )
                for row in reader
            ]
        return []

    def write(self, ressources: list[RessourceData]) -> None:
        with open(self.ressource_csv_path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(RessourceData._fields)
            writer.writerows(ressources)

    def _get_ressource_filenames(self) -> list[str]:
        return [
            filename
            for filename in os.listdir(self.dir_path)
            if isfile(join(self.dir_path, filename)) and filename.endswith(".py")
        ]

    def _create_or_get_ressource_data(
        self, filename: str, ressource_list: list[RessourceData]
    ) -> RessourceData:
        """
        This function scan the ressource_list in order to file a ressrouce with a
        matching ressource_filename and return it's score.
        Return 0 if the ressource does not exists
        """
        for ressource in ressource_list:
            if ressource.filename == filename:
                return ressource

        yesterday = (datetime.now() - timedelta(days=1)).date()
        return RessourceData(filename=filename, score=0, last_seen_date=yesterday)

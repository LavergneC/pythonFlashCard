import csv
import os
from datetime import datetime, timedelta

from main.generate_exercise_components.ressource_picker import RessourceData


class RessouceStorage:
    def __init__(self, ressource_csv_path: str, ressource_directory_path: str) -> None:
        self.dir_path = ressource_directory_path
        self.ressource_csv_path = ressource_csv_path

        old_db = []
        if os.path.exists(self.ressource_csv_path):
            old_db = self.read()

        new_ressources = [
            self._get_or_create_ressource_data(
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
        ressource_filenames = []

        for _, _, files in os.walk(self.dir_path):
            ressource_filenames += [
                filename for filename in files if filename.endswith(".py")
            ]

        return ressource_filenames

    def _get_or_create_ressource_data(
        self, filename: str, ressource_list: list[RessourceData]
    ) -> RessourceData:
        """
        This function scan the ressource_list in order to file a ressource with a
        matching ressource_filename and return it's score.
        Return 0 if the ressource does not exists
        """
        for ressource in ressource_list:
            if ressource.filename == filename:
                return ressource

        yesterday = (datetime.now() - timedelta(days=1)).date()
        return RessourceData(filename=filename, score=0, last_seen_date=yesterday)

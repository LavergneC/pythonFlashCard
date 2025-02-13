import csv
import os
from datetime import datetime, timedelta
from os.path import isfile, join

from main.generate_exercise_components.ressource_picker import RessourceData


class RessouceStorage:
    def __init__(self, ressource_csv_path: str, ressource_directory_path: str) -> None:
        self.ressource_csv_path = ressource_csv_path
        if not os.path.exists(self.ressource_csv_path):
            self._init_db(ressource_directory_path)

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

    def _init_db(self, ressource_directory_path: str) -> None:
        yesterday = (datetime.now() - timedelta(days=1)).date()

        new_ressources = [
            RessourceData(filename=file_name, score=0, last_seen_date=yesterday)
            for file_name in os.listdir(ressource_directory_path)
            if isfile(join(ressource_directory_path, file_name))
            and file_name[-3:] == ".py"
        ]

        self.write(ressources=new_ressources)

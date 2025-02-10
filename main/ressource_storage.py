import csv
from datetime import datetime

from main.constants import RESSOURCE_DB_PATH
from main.ressource_picker import RessourceData


class RessouceStorage:
    def __init__(self, ressource_csv_path: str = RESSOURCE_DB_PATH) -> None:
        self.ressource_csv_path = ressource_csv_path

    def read(self) -> list[RessourceData]:
        with open(self.ressource_csv_path, "r") as f:
            reader = csv.DictReader(f)
            return [
                RessourceData(
                    row["filename"],
                    int(row["score"]),
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

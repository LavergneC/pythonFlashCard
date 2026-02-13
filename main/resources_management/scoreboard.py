from main.resources_management.resource_picker import ResourceData, ResourcePicker


class Scoreboard:
    @staticmethod
    def scoreboard(resources: list[ResourceData]) -> str:
        worse_resources = Scoreboard._worse_resources(resources)

        base = f"Your current score is {round(worse_resources[0][1], 2)}. Because of:"
        for filename, score in worse_resources:
            base += f"\n\t-'{filename}'\t{round(score, 2)} points"

        return base

    @staticmethod
    def score(resources: list[ResourceData]) -> str:
        worse_resources = Scoreboard._worse_resources(resources)
        return f"Your current score is {round(worse_resources[0][1], 2)}"

    @staticmethod
    def _worse_resources(resources: list[ResourceData]) -> list[tuple[str, int]]:
        resource_picker = ResourcePicker(resources=resources)
        resource_picker.sort_resources()

        return [
            (resource.filename, resource.score)
            for resource in resource_picker.resources[:3]
        ]

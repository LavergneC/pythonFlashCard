# collections-defaultdict_hard.py
from collections import defaultdict  # but not that
from dataclasses import dataclass  # remove that from question


@dataclass
class SaleLine:
    city: str
    product: str
    quantity: int


class SaleManager:
    def __init__(self, initial_sale_lines: list[SaleLine]):
        self.sales_data = defaultdict(lambda: defaultdict(int))

        for sale_line in initial_sale_lines:
            self.sales_data[sale_line.city][sale_line.product] = sale_line.quantity

    def get_quantity(self, city: str, product: str):
        """
        This function will return the quantity for given parameters.
        It returns 0 if no line registered for the given parameters
        """
        return self.sales_data[city][product]

    def add_sale_line(self, sale_line: SaleLine):
        """
        Add a now sale line to the registery, either create a new line or append to the existing one
        """
        self.sales_data[sale_line.city][sale_line.product] += sale_line.quantity


def _test_setup_sale_manager():
    initial_data = [
        SaleLine("New York", "Apples", 120),
        SaleLine("New York", "Oranges", 75),
        SaleLine("Boston", "Bananas", 50),
        SaleLine("Atlanta", "Apples", 80),
        SaleLine("Miami", "Bananas", 60),
        SaleLine("Miami", "Oranges", 45),
        SaleLine("Los Angeles", "Bananas", 200),
        SaleLine("San Francisco", "Apples", 90),
    ]
    return SaleManager(initial_data)


def test_sale_datat_get_temperature():
    sale_manager = _test_setup_sale_manager()

    assert sale_manager.get_quantity(city="Boston", product="Bananas") == 50
    assert sale_manager.get_quantity(city="Boston", product="Dragon fruit") == 0
    assert sale_manager.get_quantity(city="Saint-Christophe", product="Apples") == 0


def test_sale_datat_add_sell_line():
    sale_manager = _test_setup_sale_manager()

    sale_manager = _test_setup_sale_manager()
    sale_manager.add_sale_line(SaleLine("New York", "Apples", 7))
    sale_manager.add_sale_line(SaleLine("Atlanta", "Blueberry", 10))
    sale_manager.add_sale_line(SaleLine("Bordeaux", "Pear", 140))

    assert sale_manager.get_quantity("New York", "Apples") == 127
    assert sale_manager.get_quantity("Atlanta", "Blueberry") == 10
    assert sale_manager.get_quantity("Bordeaux", "Pear") == 140

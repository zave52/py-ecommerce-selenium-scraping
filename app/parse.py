import csv
from dataclasses import dataclass, fields, astuple
from urllib.parse import urljoin

BASE_URL = "https://webscraper.io/"
HOME_URL = urljoin(BASE_URL, "test-sites/e-commerce/more/")


@dataclass
class Product:
    title: str
    description: str
    price: float
    rating: int
    num_of_reviews: int


PRODUCT_FIELDS = [field.name for field in fields(Product)]


def write_products_to_csv(csv_path: str, products: list[Product]) -> None:
    with open(csv_path, "w") as f:
        writer = csv.writer(f)
        writer.writerow(PRODUCT_FIELDS)
        writer.writerows([astuple(product) for product in products])


def get_all_products() -> None:
    pass


if __name__ == "__main__":
    get_all_products()

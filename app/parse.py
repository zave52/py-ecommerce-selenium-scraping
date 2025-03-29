import csv
from dataclasses import dataclass, fields, astuple
from urllib.parse import urljoin

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

BASE_URL = "https://webscraper.io/"
HOME_URL = urljoin(BASE_URL, "test-sites/e-commerce/more/")

COMPUTER_URL = urljoin(HOME_URL, "computers/")
PHONE_URL = urljoin(HOME_URL, "phones/")

LAPTOP_URL = urljoin(COMPUTER_URL, "laptops/")
TABLET_URL = urljoin(COMPUTER_URL, "tablets/")

TOUCH_URL = urljoin(PHONE_URL, "touch/")

URLS_TO_SCRAPE = [
    HOME_URL,
    COMPUTER_URL,
    PHONE_URL,
    LAPTOP_URL,
    TABLET_URL,
    TOUCH_URL
]


@dataclass
class Product:
    title: str
    description: str
    price: float
    rating: int
    num_of_reviews: int


PRODUCT_FIELDS = [field.name for field in fields(Product)]


def parse_single_product(product: WebElement) -> Product:
    return Product(
        title=product.find_element(By.CLASS_NAME, "title").text,
        description=product.find_element(By.CLASS_NAME, "description").text,
        price=float(
            product.find_element(By.CLASS_NAME, "price")
            .text.replace("$", "")
        ),
        rating=int(
            product.find_element(By.CLASS_NAME, "review-count")
            .text.split()[0]
        ),
        num_of_reviews=len(
            product.find_elements(By.CLASS_NAME, "ws-icon-star")
        )
    )


def write_products_to_csv(csv_path: str, products: list[Product]) -> None:
    with open(csv_path, "w") as f:
        writer = csv.writer(f)
        writer.writerow(PRODUCT_FIELDS)
        writer.writerows([astuple(product) for product in products])


def get_all_products() -> None:
    pass


if __name__ == "__main__":
    get_all_products()

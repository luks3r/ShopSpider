from scrapy.spiders import Spider
from sql_spider.items import ComputerItem
import re

PRICE_PATTERN = re.compile("\d+(?:[.,]\d+)?")


def parse_price(price: str) -> float:
    formatted_price = price.replace(u'\xa0', u'').replace(",", ".")
    match = re.match(PRICE_PATTERN, formatted_price)

    if not match:
        raise ValueError("Invalid price format")

    return float(match.group(0))


class OrdiSpider(Spider):
    name = "ordispider"
    start_urls = ["https://ordi.eu/lauaarvutid/"]

    def parse(self, response):
        for product in response.css(".item"):
            price = product.css(".price-box > span::text").get()
            yield ComputerItem(
                title=product.css(".product-name > a::attr(title)").get(),
                price=parse_price(price),
                picture=product.css(".product-image > img::attr(src)").get()
            )

        next_page = response.css("a.next::attr(href)").get()
        print(f"==================================NEXT_PAGE ========================================\nUrl: '{next_page}'")
        if next_page is not None:
            print("Going")
            yield response.follow(next_page, callback=self.parse)

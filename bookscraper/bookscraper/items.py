# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BookscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

# now here we are going to select the which item we need in the data block
class BookItem(scrapy.Item):
    # id = scrapy.Field()
    url  = scrapy.Field()
    title = scrapy.Field()
    category = scrapy.Field()
    type = scrapy.Field()
    price = scrapy.Field()
    stock = scrapy.Field()
    price_excl_tax = scrapy.Field()
    price_incl_tax = scrapy.Field()
    stars = scrapy.Field()
    description = scrapy.Field()


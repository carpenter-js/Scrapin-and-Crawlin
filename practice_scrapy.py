import scrapy

# Tutorial:
# https://www.digitalocean.com/community/tutorials/how-to-crawl-a-web-page-with-scrapy-and-python-3

class BrickSetSpider(scrapy.Spider):
    name = 'brickset_spider'
    start_urls = ['https://brickset.com/sets/year-2016']

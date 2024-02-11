from scrapy.crawler import CrawlerProcess
from quotes_scraper.spiders.quotes import QuotesSpider
from quotes_scraper.spiders.authors import AuthorsSpider

if __name__ == '__main__':
    process = CrawlerProcess()
    process.crawl(QuotesSpider)
    process.crawl(AuthorsSpider)
    process.start()

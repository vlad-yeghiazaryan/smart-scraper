from scrapy.utils.project import get_project_settings
from smartScraper.spiders.mainSpider import SmartSpider
import logging
import json
import scrapydo

def main(request):
    scrapydo.setup()
    scrapydo.default_settings.update(get_project_settings())
    logging.basicConfig(level=logging.DEBUG)
    results = scrapydo.run_spider(SmartSpider, request=request)
    data = { 'Massage': 'Scraping complete.', 
    'scraped_data': results
    }
    return data

if __name__ == '__main__':
    with open('./scrape/request8.json', 'r') as f:
        request = json.loads(f.read())
        main(request)

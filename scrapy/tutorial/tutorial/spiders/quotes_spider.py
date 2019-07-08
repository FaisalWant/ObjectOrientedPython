import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"             # identifies the Spider. It must be unique within a project

    def start_requests(self):    #must return an iterable of Requests (you can return a list of requests 
                                 #or write a generator function) which the Spider will begin to crawl from. 
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):     #a method that will be called to handle the response 
                                   #downloaded for each of the requests made           
                                   # The parse() method usually parses the response,
                                   #extracting the scraped data as dicts 

        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
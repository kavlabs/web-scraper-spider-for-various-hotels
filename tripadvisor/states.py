import scrapy 
import json
import csv
import os.path
import os

# file_exists = os.path.isfile('wyndham.csv')
  
class ExtractUrls(scrapy.Spider): 
    name = "states"
  
    def start_requests(self): 
        headers = {
            "Host": "en.wikipedia.org",
            "Connection": "keep-alive",
            "Cache-Control": "max-age=0",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "DNT": "1",
            "Accept-Encoding": "gzip, deflate, sdch",
            "Accept-Language":"en-US,en;q=0.8"
        }
        urls = [ 'https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States' ] 
        # with open('kk.txt','r+') as f:
        #     urls.append(f.readlines())

        for url in urls: 
            yield scrapy.Request(url = url, callback = self.parse, headers = headers) 
  
    def parse(self, response):
        hxs = scrapy.Selector(response)
        all_links = hxs.xpath('*//a/@href').extract()
        for link in all_links:
            # if 'hotel-details' in link:
            print(link)
                # with open('kk1.txt','a+') as f:
                #     if burl not in link:
                #         f.write(burl+link+'\n')
                #     else:
                #         f.write(link+'\n')
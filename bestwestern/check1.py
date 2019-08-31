import scrapy 
import json
import csv
import os.path
import os
burl = 'https://www.bestwestern.com'
class ExtractUrls(scrapy.Spider): 
    name = "check1"
  
    def start_requests(self): 
        headers = {
            "Host": "www.bestwestern.com",
            "Connection": "keep-alive",
            "Cache-Control": "max-age=0",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "DNT": "1",
            "Accept-Encoding": "gzip, deflate, sdch",
            "Accept-Language":"en-US,en;q=0.8"
        }
        # urls = [ 'https://www.bestwestern.com//en_US/hotels/destinations/united-states/gulf-coast/alabama/visit.html' ] 
        urls = []
        with open('kk.txt','r+') as f:
            urls.append(f.readlines())

        # with open('wyndham.csv', 'a+') as csvfile:
        #     fieldnames = ['hotel_name', 'hotel_address','hotel_city','hotel_state','hotel_zipcode','hotel_phone']
        #     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        #     writer.writeheader()
          
        for url in urls[0]: 
            yield scrapy.Request(url = url[:-1], callback = self.parse, headers = headers) 
  
    def parse(self, response):
        # p = str(response.body)
        hxs = scrapy.Selector(response)
        all_links = hxs.xpath('*//a/@href').extract()
        for link in all_links:
            if 'hotel-details' in link:
                print(burl+link)
                with open('kk1.txt','a+') as f:
                    if burl not in link:
                        f.write(burl+link+'\n')
                    else:
                        f.write(link+'\n')
        
        # with open('kk.html','wb') as f:
        #     f.write(response.body)
        # self.log("saved file")
          
        # Extra feature to get title 
        # title = response.css('title::text').extract_first()  
          
        # # Get anchor tags 
        # links = response.css('a::attr(href)').extract()      
          
        # for link in links: 
        #     yield 
        #     { 
        #         'title': title, 
        #         'links': link 
        #     } 
              
        #     if 'geeksforgeeks' in link:          
        #         yield scrapy.Request(url = link, callback = self.parse)
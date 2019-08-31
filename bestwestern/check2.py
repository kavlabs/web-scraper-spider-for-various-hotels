import scrapy 
import json
import csv
import os.path
import os
burl = 'https://www.bestwestern.com'
class ExtractUrls(scrapy.Spider): 
    name = "check2"
  
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
        # urls = [ 'https://www.bestwestern.com/en_US/book/hotel-details.49033.html' ] 
        urls = []
        with open('kk1.txt','r+') as f:
            urls.append(f.readlines())
          
        for url in urls[0]: 
            yield scrapy.Request(url = url[:-1], callback = self.parse, headers = headers) 
  
    def parse(self, response):
        try:
            p = response.xpath('//div[@class = "hotelDetailsContainer container-fluid"]/@data-hoteldetails').extract_first()
            j = json.loads(p)
            hotel_name = j['summary']['name']
            hotel_addr = j['summary']['address1']
            hotel_city = j['summary']['city']
            hotel_phone = j['summary']['phoneNumber']
            hotel_zip = j['summary']['postalCode']
            hotel_state = j['summary']['state']

            with open('bestwestern.csv', 'a+') as writeFile:
                fieldnames = ['hotel_name', 'hotel_address','hotel_city','hotel_state','hotel_zipcode','hotel_phone']
                file_is_empty = os.stat('bestwestern.csv').st_size == 0
                writer = csv.DictWriter(writeFile, fieldnames=fieldnames)
                if file_is_empty:
                    writer.writeheader()
                writer.writerow({'hotel_name':hotel_name, 'hotel_address':hotel_addr,'hotel_city':hotel_city,'hotel_state':hotel_state,'hotel_zipcode':hotel_zip,'hotel_phone':hotel_phone})
        except:
            pass
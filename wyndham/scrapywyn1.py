import scrapy 
import json
import csv
import os.path
import os

# file_exists = os.path.isfile('wyndham.csv')
  
class ExtractUrls(scrapy.Spider): 
    name = "wyn"
  
    def start_requests(self): 
        headers = {
            "Host": "www.wyndhamhotels.com",
            "Connection": "keep-alive",
            "Cache-Control": "max-age=0",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "DNT": "1",
            "Accept-Encoding": "gzip, deflate, sdch",
            "Accept-Language":"en-US,en;q=0.8"
        }
        urls = [] 
        with open('kk.txt','r+') as f:
            urls.append(f.readlines())

        for url in urls[0]: 
            yield scrapy.Request(url = url[:-1], callback = self.parse, headers = headers) 
  
    def parse(self, response):
        p = str(response.body)
        start = p.find('"application/ld+json">')+len('"application/ld+json">')+2
        end = p.find('<script type="text/javascript" src="/javascript/config.js">')-13
        k = str(p[start:end]).replace(r"\n","").replace(r"\t","")
        j = json.loads(k)
        hotel_name = j['name']
        print(hotel_name)
        hotel_addr = j['address']['streetAddress']
        hotel_city = j['address']['addressLocality']
        hotel_state = j['address']['addressRegion']
        hotel_zip = j['address']['postalCode']
        hotel_phone = j['telephone']
        with open('wyndham.csv', 'a+') as writeFile:
            fieldnames = ['hotel_name', 'hotel_address','hotel_city','hotel_state','hotel_zipcode','hotel_phone']
            file_is_empty = os.stat('wyndham.csv').st_size == 0
            writer = csv.DictWriter(writeFile, fieldnames=fieldnames)
            if file_is_empty:
                writer.writeheader()
            writer.writerow({'hotel_name':hotel_name, 'hotel_address':hotel_addr,'hotel_city':hotel_city,'hotel_state':hotel_state,'hotel_zipcode':hotel_zip,'hotel_phone':hotel_phone})
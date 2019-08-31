import scrapy 
import json
import csv
import os.path
import os
class ExtractUrls(scrapy.Spider): 
    name = "stay"
  
    def start_requests(self): 
        headers = {
            "Host": "www.staystudio6.com",
            "Connection": "keep-alive",
            "Cache-Control": "max-age=0",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "DNT": "1",
            "Accept-Encoding": "gzip, deflate, sdch",
            "Accept-Language":"en-US,en;q=0.8"
        }
          
        for i in range(100000): 
            url = 'https://www.staystudio6.com/var/g6/hotel-information/en/'+'{}'.format(i+1)+'.json'
            yield scrapy.Request(url = url, callback = self.parse, headers = headers) 
  
    def parse(self, response):
        try:
            p = json.loads(response.body)
            # print(p)
            hotel_addr = p['address']
            hotel_phone = p['phone']
            hotel_name = p['name']
            hotel_city = p['city']
            hotel_zip = p['zip']
            hotel_state = p['state']
            with open('staystudio6.csv', 'a+') as writeFile:
                fieldnames = ['hotel_name', 'hotel_address','hotel_city','hotel_state','hotel_zipcode','hotel_phone']
                file_is_empty = os.stat('staystudio6.csv').st_size 
                writer = csv.DictWriter(writeFile, fieldnames=fieldnames)
                if file_is_empty == 0:
                    writer.writeheader()
                writer.writerow({'hotel_name':"staystudio6"+" "+hotel_name, 'hotel_address':hotel_addr,'hotel_city':hotel_city,'hotel_state':hotel_state,'hotel_zipcode':hotel_zip,'hotel_phone':hotel_phone})
        except:
            pass
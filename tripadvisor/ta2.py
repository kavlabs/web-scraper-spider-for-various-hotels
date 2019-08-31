import scrapy 
import json
import csv
import os.path
import os
  
class ExtractUrls(scrapy.Spider): 
    name = "ta2"
    # start_urls = [] 
    with open("kk.txt", "rt") as f:
        start_urls = [url.strip() for url in f.readlines()]
  
    def parse(self, response):
        hxs = scrapy.Selector(response)
        text1 = hxs.xpath('//script[@type="application/ld+json"]/text()').extract_first()
        phone = hxs.xpath('//*[@id="taplc_resp_hr_atf_hotel_info_0"]/div/div[2]/div/div[2]/div/div[2]/a/span[2]/text()').extract_first()
        hotel_phone = phone
        j = json.loads(text1)
        hotel_name = j['name']
        hotel_addr = j['address']['streetAddress']
        hotel_city = j['address']['addressLocality']
        hotel_state = j['address']['addressRegion']
        hotel_zip = j['address']['postalCode']
        with open('tripadvisor.csv', 'a+') as writeFile:
            fieldnames = ['hotel_name', 'hotel_address','hotel_city','hotel_state','hotel_zipcode','hotel_phone']
            file_is_empty = os.stat('tripadvisor.csv').st_size == 0
            writer = csv.DictWriter(writeFile, fieldnames=fieldnames)
            if file_is_empty:
                writer.writeheader()
            writer.writerow({'hotel_name':hotel_name, 'hotel_address':hotel_addr,'hotel_city':hotel_city,'hotel_state':hotel_state,'hotel_zipcode':hotel_zip,'hotel_phone':hotel_phone})
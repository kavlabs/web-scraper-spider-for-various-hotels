import scrapy 
import json
import csv
import os.path
import os
import requests
burl = 'https://www.wyndhamhotels.com/'
hotels = ['americinn','baymont','caesars-entertainment','days-inn','dolce','hawthorn-extended-stay','hojo','laquinta','microtel','ramada','super-8','trademark','travelodge','tryp','wingate','wyndham-garden','wyndham-grand','wyndham','wyndham-vacations']
class ExtractUrls(scrapy.Spider): 
    name = "kk"
  
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
          
        for i in range(15): 
            url = 'https://www.wyndhamhotels.com/BWSServices/services/search/properties?recordsPerPage=500&pageNumber='+'{}'.format(i+1)+'&brandId=ALL&countryCode=US'
            # url = 'https://www.wyndhamhotels.com/BWSServices/services/search/properties?recordsPerPage=500&pageNumber=1&brandId=ALL&countryCode=US'
            yield scrapy.Request(url = url, callback = self.parse, headers = headers) 

    def parse(self, response):
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
            with requests.Session() as s:
                p = requests.get(response.request.url, headers = headers)
                print(p.content.decode('utf-8'))
                k = json.loads(p.content.decode('utf-8'))
                for i in range(k['countries'][0]['statesCount']):
                    for j in range(k['countries'][0]['states'][i]['citiesCount']):
                        for m in range(k['countries'][0]['states'][i]['cities'][j]['totalPropertyCount']):
                            h = k['countries'][0]['states'][i]['cities'][j]['propertyList'][m]['brand'].lower()
                            s = ''
                            for item in hotels:
                                if item[:2] in h:
                                    s = item
                            p = k['countries'][0]['states'][i]['cities'][j]['cityName'].lower()+'-'+k['countries'][0]['states'][i]['stateName'].lower()
                            t = k['countries'][0]['states'][i]['cities'][j]['propertyList'][m]['uniqueUrl'].lower()
                            kk = burl + s + '/' + p + '/' + t + '/overview'
                            print(kk)
                            with open('kk.txt','a+') as o:
                                o.write(kk+'\n')
                                o.close()
        except:
            pass
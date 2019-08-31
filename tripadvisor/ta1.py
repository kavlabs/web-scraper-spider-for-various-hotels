import scrapy 
from scrapy.http import FormRequest
import json
import csv
import os.path
import os

old_url = ''
urls_list = ['https://www.tripadvisor.com/Hotels-g28922-Alabama-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28923-Alaska-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28924-Arizona-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28925-Arkansas-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28926-California-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28927-Colorado-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28928-Connecticut-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28929-Delaware-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28930-Florida-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28931-Georgia-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28932-Hawaii-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28933-Idaho-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28934-Illinois-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28935-Indiana-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28936-Iowa-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28937-Kansas-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28938-Kentucky-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28939-Louisiana-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28940-Maine-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28941-Maryland-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28942-Massachusetts-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28943-Michigan-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28944-Minnesota-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28945-Mississippi-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28946-Missouri-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28947-Montana-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28948-Nebraska-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28949-Nevada-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28950-New_Hampshire-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28951-New_Jersey-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28952-New_Mexico-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28953-New_York-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28954-North_Carolina-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28955-North_Dakota-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28956-Ohio-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28957-Oklahoma-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28958-Oregon-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28959-Pennsylvania-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28960-Rhode_Island-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28961-South_Carolina-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28962-South_Dakota-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28963-Tennessee-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28964-Texas-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28965-Utah-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28966-Vermont-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28967-Virginia-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28968-Washington-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28969-West_Virginia-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28970-Wisconsin-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28971-Wyoming-Hotels.html']
i=[0]*len(urls_list)
class ExtractUrls(scrapy.Spider): 
    name = "ta1"
    allowed_domains = ['tripadvisor.com']
    start_urls = ['https://www.tripadvisor.com/Hotels-g28922-Alabama-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28923-Alaska-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28924-Arizona-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28925-Arkansas-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28926-California-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28927-Colorado-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28928-Connecticut-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28929-Delaware-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28930-Florida-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28931-Georgia-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28932-Hawaii-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28933-Idaho-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28934-Illinois-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28935-Indiana-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28936-Iowa-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28937-Kansas-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28938-Kentucky-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28939-Louisiana-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28940-Maine-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28941-Maryland-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28942-Massachusetts-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28943-Michigan-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28944-Minnesota-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28945-Mississippi-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28946-Missouri-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28947-Montana-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28948-Nebraska-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28949-Nevada-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28950-New_Hampshire-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28951-New_Jersey-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28952-New_Mexico-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28953-New_York-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28954-North_Carolina-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28955-North_Dakota-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28956-Ohio-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28957-Oklahoma-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28958-Oregon-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28959-Pennsylvania-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28960-Rhode_Island-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28961-South_Carolina-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28962-South_Dakota-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28963-Tennessee-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28964-Texas-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28965-Utah-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28966-Vermont-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28967-Virginia-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28968-Washington-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28969-West_Virginia-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28970-Wisconsin-Hotels.html', 'https://www.tripadvisor.com/Hotels-g28971-Wyoming-Hotels.html']

  
    def parse(self, response):
        if len(response.xpath('/html/body//*')) <= 1000:
           return
        for href in response.xpath('*//a/@href'):
            url = response.urljoin(href.extract())
            if 'Hotel_Review' in url and '#REVIEWS' not in url:
                print(url.replace(".in",".com"))
                if os.path.isfile("kk.txt")!=True:
                    open("kk.txt", "a+")
                with open("kk.txt", "r+") as file:
                    for line in file:
                        if url.replace(".in",".com") in line:
                           break
                    else:
                        file.write(url.replace(".in",".com")+'\n')
        global i
        global old_url
        global urls_list
        try:
            u = response.request.url[response.request.url.find("tripadvisor.")+12:response.request.url.find("/Hotels-")]
            print('------------------------------------------------------------------')
            print(u)
            print(response.request.url)
            url2 = response.request.url.replace(u,"com")
            index_i = urls_list.index(str(url2))
            i[index_i]+=30
            body = f'plSeed=806989682&offset={i[index_i]}&reqNum=2&isLastPoll=false&paramSeqId=4&waitTime=2560&changeSet=&puid=XPu69QokK2gABqFjTpAAAABW'
            print(body)
            yield scrapy.Request(url2,
                method='POST',
                body=body,
                headers={'X-Requested-With': 'XMLHttpRequest','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
                callback=self.parse, dont_filter=True)
        except Exception as e:
            # print(e)
            None
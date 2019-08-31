import scrapy
import csv
class Choicehotels2Spider(scrapy.Spider):
    name = 'choicehotels2'
    allowed_domains = ['choicehotels.com']
    
    # with open("urls.txt", "rt") as f:
    #     start_urls = [url.strip() for url in f.readlines()]
    # f = open("urls.txt")
    # start_urls = [url.strip() for url in f.readlines()]
    # f.close
    start_urls = []
    with open('choiceinput.csv','r+') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for r in csv_reader:
            start_urls.append(r[0])

    def parse(self, response):
        pass
        main = response.xpath('//*[@class="more-content"]')
        for data in main:
            choicename = response.xpath('//*[@class="more-content"]/p/a/text()').extract()
            choiceaddress = response.xpath('//*[@class="more-content"]/p/br[1]/following::text()[1]').extract()
            choicecitystatezip = response.xpath('//*[@class="more-content"]/p/br[2]/following::text()[1]').extract()
            choicephone = response.xpath('//*[@class="more-content"]/p/br[3]/following::text()[1]').extract()
                

            yield{'Name': choicename,
                'Address': choiceaddress,
                'CityStateZip': choicecitystatezip,
                'Phone': choicephone}
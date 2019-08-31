import scrapy 
import json
import csv
import os.path
import os
list1 = ['/en_US/hotels/destinations/united-states/orlando-hotels.html',
'/en_US/hotels/destinations/united-states/anaheim-hotels.html',
'/en_US/hotels/destinations/united-states/san-diego-hotels.html',
'/en_US/hotels/destinations/united-states/nashville-hotels.html',
'/en_US/hotels/destinations/united-states/new-orleans-hotels.html',
'/en_US/hotels/destinations/united-states/hotels-in-myrtle-beach.html',
'/en_US/hotels/destinations/united-states/boston-hotels.html',
'/en_US/hotels/destinations/united-states/gulf-coast/hotels-texas/greater-houston-area/houston-hotels.html',
'/en_US/hotels/destinations/united-states/hotels-in-miami.html',
'/en_US/hotels/destinations/united-states/gulf-coast/hotels-texas/metroplex/hotels-in-dallas.html',
'/en_US/hotels/destinations/united-states/virginia-beach-hotels.html',
'/en_US/hotels/destinations/united-states/chicago-hotels.html',
'/en_US/hotels/destinations/united-states/monterey-hotels.html',
'/en_US/hotels/destinations/united-states/gulf-coast/hotels-texas/san-antonio-southern-plains/san-antonio-hotels.html',
'/en_US/hotels/destinations/united-states/santa-barbara-hotels.html',
'/en_US/hotels/destinations/united-states/san-francisco-hotels.html',
'/en_US/hotels/destinations/united-states/hotels-in-new-york.html',
'/en_US/hotels/destinations/united-states/los-angeles-hotels.html',
'/en_US/hotels/destinations/united-states/las-vegas-hotels.html']
burl = 'https://www.bestwestern.com'
# file_exists = os.path.isfile('wyndham.csv')
  
class ExtractUrls(scrapy.Spider): 
    name = "check"
  
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
        urls = [ 'https://www.bestwestern.com/en_US/hotels/destinations/united-states.html' ] 
        # with open('kk.txt','r+') as f:
        #     urls.append(f.readlines())

        # with open('wyndham.csv', 'a+') as csvfile:
        #     fieldnames = ['hotel_name', 'hotel_address','hotel_city','hotel_state','hotel_zipcode','hotel_phone']
        #     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        #     writer.writeheader()
          
        for url in urls: 
            yield scrapy.Request(url = url, callback = self.parse, headers = headers) 
  
    def parse(self, response):
        # p = str(response.body)
        hxs = scrapy.Selector(response)
        all_links = hxs.xpath('*//a/@href').extract()
        for link in all_links:
            if 'hotels/destinations/united-states' in link and 'https://www.bestwestern.com/' not in link and link not in list1:
            	print(burl+link[:-5]+'/visit.html')
            	with open('kk.txt','a+') as f:
            		f.write(burl+link[:-5]+'/visit.html'+'\n')
        # start = p.find('"application/ld+json">')+len('"application/ld+json">')+2
        # end = p.find('<script type="text/javascript" src="/javascript/config.js">')-13
        # # k = "'''"+str(p[start:end]).replace(" ","").replace(r"\n","")+"'''"
        # k = str(p[start:end]).replace(" ","").replace(r"\n","").replace(r"\t","")
        # # print(k)
        # j = json.loads(k)
        # hotel_name = j['name']
        # print(hotel_name)
        # hotel_addr = j['address']['streetAddress']
        # hotel_city = j['address']['addressLocality']
        # hotel_state = j['address']['addressRegion']
        # hotel_zip = j['address']['postalCode']
        # hotel_phone = j['telephone']
        # # hotel_url = url
        # # print(hotel_url)
        # # writer.writerow({'hotel_name':hotel_name, 'hotel_address':hotel_addr,'hotel_city':hotel_city,'hotel_state':hotel_state,'hotel_zipcode':hotel_zip,'hotel_phone':hotel_phone,'hotel_url':hotel_url})
        # with open('wyndham.csv', 'a+') as writeFile:
        #     fieldnames = ['hotel_name', 'hotel_address','hotel_city','hotel_state','hotel_zipcode','hotel_phone']
        #     file_is_empty = os.stat('wyndham.csv').st_size == 0
        #     writer = csv.DictWriter(writeFile, fieldnames=fieldnames)
        #     if file_is_empty:
        #         writer.writeheader()
        #     # if not file_exists:
        #     #     writer.writeheader()
        #     writer.writerow({'hotel_name':hotel_name, 'hotel_address':hotel_addr,'hotel_city':hotel_city,'hotel_state':hotel_state,'hotel_zipcode':hotel_zip,'hotel_phone':hotel_phone})

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
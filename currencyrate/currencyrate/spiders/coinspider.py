import scrapy
from datetime import datetime


class CoinSpider(scrapy.Spider):
    name = "coins"

    def start_requests(self):
        url = 'https://www.forex.pk/open_market_rates.asp'
        
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
            path="//table[@cellspacing=2]/tr[contains(., '%s')]/td[3]/text()"
            # result = {'USD' : path % 'USD',
            # 'CAD' : path % 'CAD',
            # 'QAR' : path % 'QAR',
            # 'EUR' : path % 'EUR',
            # 'CNY' : path % 'CNY'}
            date=datetime.now()
            date=date.strftime("%d-%m-%Y")
            # with open('coins.json', 'a') as f:
            #         f.write(f"""

            #             {date}
            #             """)
                        
            # for i in result:
            #     value = response.xpath(result[i]).getall()
            yield{  'date' : date,
                    'USD' :response.xpath(path % 'USD' ).getall(),
                    'QAR' :response.xpath(path % 'QAR' ).getall(),
                    'CAD' :response.xpath(path % 'CAD' ).getall(),
                    'EUR' :response.xpath(path % 'EUR' ).getall(),
                    'CNY' :response.xpath(path % 'CNY' ).getall()
                    }
                        # f.write(f'''
                        # {i} : {value[0]} PKR''')
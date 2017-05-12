from scrapy import Spider
from scrapy.selector import Selector
from datainfo.items import DatainfoItem


class DatainfoSpider(Spider):
	name = "dataone"
	allowed_domains = ["https://data.gov.in/"]
	start_urls = ["https://data.gov.in/catalogs#sort_by=created&sort_order=DESC&items_per_page=9&page=4",]

	def parse(self,response):
		item = DatainfoItem()
		item['title'] = Selector(response).xpath('//*[@class="region region-content"]//*[@class="views-field views-field-title"]//*[@class="field-content"]/a/text()').extract()
		item['datasets'] = Selector(response).xpath('//span[@class="count-resource"]/text()').extract()
		item['visual_access'] = Selector(response).xpath('//span[@class="count-vis"]/text()').extract()
		item['last_updated'] = Selector(response).xpath('//div[@class="views-field views-field-changed"]/span[@class="field-content"]/text()').extract()
		item['views'] = Selector(response).xpath('//span[@class="catalog-bottom-views"]/text()').extract()
		item['downloads'] = Selector(response).xpath('//div[@class="views-field views-field-field-file-download-count"]/div[@class="field-content"]/text()').extract()
		item['ministry'] = Selector(response).xpath('//div[@class="views-field views-field-field-ministry-department"]/span[@class="field-content"]/text()').extract()
		yield item
import django
django.setup()
from django.core.management.base import BaseCommand
from CEVA_shipment_track.spiders import ceva_shipmentSpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

class Command(BaseCommand):
	help="Release the spiders"

	def handle(self,*args,**options):
		process=CrawlerProcess(get_project_settings())
		process.crawl(ceva_shipmentSpider)
		process.start()	

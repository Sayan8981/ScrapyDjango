# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import sys
DJANGO_PROJECT_PATH='/home/saayan-0186/ScrapyDjango/CEVA_shipment'
sys.path.insert(0,DJANGO_PROJECT_PATH)
import scrapy,django
import ceva 
import scrapy_djangoitem
from scrapy_djangoitem import DjangoItem, Field
from ceva.models import CevaShipmentDetail


class CevaShipmentTrackItem(DjangoItem):
    # define the fields for your item here like:
    django_model=CevaShipmentDetail

# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import sys
#import pdb;pdb.set_trace()
import scrapy,django 
import scrapy_djangoitem
from scrapy_djangoitem import DjangoItem, Field
from ceva.models import CevaShipmentDetail


class CevaShipmentTrackItem(DjangoItem):
    # define the fields for your item here like:
    django_model=CevaShipmentDetail

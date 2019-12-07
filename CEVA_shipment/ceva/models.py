# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CevaShipmentDetail(models.Model):
    waybill_number = models.CharField(primary_key=True, max_length=100)
    ship_date = models.CharField(max_length=100, blank=True, null=True)
    due_date = models.CharField(max_length=200, blank=True, null=True)
    estimated_delivery_date = models.CharField(max_length=100, blank=True, null=True)
    shipper_location = models.CharField(max_length=100, blank=True, null=True)
    consignee_location = models.CharField(max_length=100, blank=True, null=True)
    total_pcs = models.CharField(max_length=200, blank=True, null=True)
    actual_weight = models.CharField(max_length=1000, blank=True, null=True)
    charge_weight = models.CharField(max_length=200, blank=True, null=True)
    freight_terms = models.CharField(max_length=100, blank=True, null=True)
    service_level = models.CharField(max_length=100, blank=True, null=True)
    delivery_type = models.CharField(max_length=100, blank=True, null=True)
    movement_type = models.CharField(max_length=100, blank=True, null=True)
    history_data = models.CharField(max_length=5000, blank=True, null=True)

     
    class Meta:
        ordering=["waybill_number"]
   
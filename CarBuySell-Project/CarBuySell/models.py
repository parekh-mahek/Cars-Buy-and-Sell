from django.db import models
import datetime
import os

def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/', filename)

class Members(models.Model):
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

class cars(models.Model):
    email = models.CharField(max_length=255)
    compmodel = models.CharField(max_length=255)
    Present_Price = models.CharField(max_length=255)
    Kms_Driven = models.CharField(max_length=255)
    Owner = models.CharField(max_length=255)
    Age = models.CharField(max_length=255)
    Fuel_Type = models.CharField(max_length=255)
    Seller_Type = models.CharField(max_length=255)
    Transmission = models.CharField(max_length=255)
    Pred_Price = models.CharField(max_length=255)
    image=models.ImageField(upload_to=filepath, null=True, blank=True)
    own_exp_price=models.CharField(max_length=255, null=True, blank=True)

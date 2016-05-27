from __future__ import unicode_literals
from django.db import models
from django.utils import timezone



# Create your models here.


class HotelInfo(models.Model):
    HotelID = models.TextField(db_column='hotelID', blank=True,primary_key=True)  # Field name made lowercase.
    Destination=models.TextField(db_column='destination', blank=True, null=True)  # Field name made lowercase.
    Area=models.TextField(db_column='area', blank=True, null=True)  # Field name made lowercase.
    HotelName=models.TextField(db_column='HotelName', blank=True, null=True)  # Field name made lowercase.
    HotelAddress=models.TextField(db_column='address', blank=True, null=True)  # Field name made lowercase.   HotelAmenities(JSON)
    HotelAmens= models.TextField(db_column='hotelAmenities', blank=True, null=True)  # Field name made lowercase.
    HotelServices=models.TextField(db_column='hotelServices', blank=True, null=True)  # Field name made lowercase.
    HotelRoomTypes=models.TextField(db_column='hotelRoomTypes', blank=True, null=True)  # Field name made lowercase.(JSON)
    PriceByDate=models.TextField(db_column='PriceByDate', blank=True, null=True)  # Field name made lowercase.(From)
    HotelPictures=models.ImageField(upload_to="hotelPics/",default="hotelPics/avatar.jpg")  # Field name made lowercase.(HTML)
    ownerId=models.TextField(db_column='ownerId',default='Overnight')

    class Meta:
        managed = True
        db_table = 'HotelInfo'


class Roominfo(models.Model):
    roomid = models.AutoField(primary_key=True)
    roomType=models.TextField(db_column="RoomType",blank=True)
    HotelName = models.TextField(db_column='HotelName', blank=True, null=True)  # Field name made lowercase.
    Destination = models.TextField(db_column='destination', blank=True, null=True)  # Field name made lowercase.
    date=models.DateField(null=True,blank=True)
    ratePerNight=models.FloatField()
    packagePrice=models.FloatField()
    discountPercent=models.FloatField()
    transport=models.FloatField(default=0.0)
    ownerId=models.TextField(db_column='ownerId',default='Overnight')


    class Meta:
        managed=True
        db_table='Roominfo'

class Package(models.Model):
    packageId=models.AutoField(primary_key=True)
    packagename=models.TextField(db_column='packagename')
    packagedesc=models.TextField(db_column="desc")
    price=models.FloatField(db_column="price",default=0.0)
    roomType = models.TextField(db_column="RoomType", blank=True)
    serviceList=models.TextField(db_column="serviceList")

    class Meta:
        managed=True
        db_table='Package'
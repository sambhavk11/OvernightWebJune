from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django import template

register=template.Library()

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

    @register.filter(name='serviceparse')
    def serviceparse(val):
        return val.split(",")


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

class Traveller(models.Model):
    miles=models.IntegerField(default=0)
    worldpercent=models.IntegerField(default=0)
    cityCount=models.IntegerField(default=0)
    trips=models.IntegerField(default=0)
    countryCount=models.IntegerField(default=0)
    location=models.TextField(default= " ")
    fname=models.TextField(default= " ")
    lname=models.TextField(default= " ")
    email=models.TextField(default= " ")
    phone=models.TextField(default=" ")
    homeAirport=models.TextField(default=" ")
    streetAddr=models.TextField(default=" ")
    unit=models.TextField(default=" ")
    city=models.TextField(default= " ")
    state=models.TextField(default= " ")
    gender=models.TextField(default="male")
    zip=models.TextField(default=" ")
    country=models.TextField(default=" ")

    class Meta:
        managed=True
        db_table="Traveller"

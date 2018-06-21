from __future__ import unicode_literals

from django.db import models

# Create your models here.

class UberTripManager(models.Manager):
    def validate_trip(self, postData):
        messages = []
        day = postData['day']
        if len(str(day)) < 1:
            messages.append("Please enter a valid day of the month!")
        month = postData['month']
        if len(str(month)) < 1:
            messages.append("Please enter a valid month!")
        year = postData['year']
        if len(str(year)) < 1:
            messages.append("Please enter a valid year!")
        start_hour = postData['start_hour']
        if len(str(start_hour)) < 1:
            messages.append("Please enter a starting hour for your trip!")
        start_minute = postData['start_minute']
        if len(str(start_minute)) < 1:
            messages.append("Please enter a valid starting minute for your trip!")
        am_pm = postData['am_pm']
        if len(str(am_pm)) < 1:
            messages.append("Please Enter AM or PM for the starting time of your trip!")
        start_address = postData['start_address']
        if len(str(start_address)) < 1:
            messages.append("Please enter a starting address for your trip!")
        end_address = postData['end_address']
        if len(str(end_address)) < 1:
            messages.append("Please enter an ending address for your trip!")
        fare = postData['fare']
        if len(str(fare)) < 1:
            messages.append("Please add the fare paid to you for your trip!")
        miles_driven = postData['miles_driven']
        if len(str(miles_driven)) < 1:
            messages.append("Please enter the miles driven on your trip")
        else:
            UberTrip.objects.create(day=day, month=month, year=year, start_hour=start_hour, start_minute=start_minute, am_pm=am_pm, start_address=start_address, end_address=end_address, fare=fare, miles_driven=miles_driven)
        return messages


class UberTrip(models.Model):
    day = models.IntegerField()
    month = models.IntegerField()
    year = models.IntegerField(default=2017)
    start_hour = models.IntegerField()
    start_minute = models.IntegerField()
    am_pm = models.CharField(max_length=2)
    start_address = models.CharField(max_length=200)
    end_address = models.CharField(max_length=200)
    fare = models.FloatField()
    miles_driven = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UberTripManager()

def __unicode__(self):
    return "Date: {}-{}-{}, Start Time: {}:{} {}, Start Address: {}, End Address: {}, Fare: {}, Miles Driven: {}".format(day, month, year, start_hour, start_minute, am_pm, start_address, end_address, fare, miles_driven)
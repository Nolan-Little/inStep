from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Organization(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=400)
    user = models.ManyToManyField(User)

class EventTemplate(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    description = models.CharField(max_length=150)
    venue = models.CharField(max_length=75)
    name = models.CharField(max_length=150)
    location = models.CharField(max_length=200)

class ShiftTemplate(models.Model):
    event_template = models.ForeignKey(EventTemplate, on_delete=models.CASCADE, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    num_volunteers = models.PositiveIntegerField()
    description = models.CharField(max_length=100)

class ScheduledEvent(models.Model):
    event_template = models.ForeignKey(EventTemplate, on_delete=models.CASCADE)
    date = models.DateField()
    sign_up_url = models.URLField(max_length=200)

class Volunteer(models.Model):
    name = models.CharField(max_length=150, default="volunteer")

class ScheduledShift(models.Model):
    scheduled_event = models.ForeignKey(ScheduledEvent, on_delete=models.CASCADE)
    shift_template = models.ForeignKey(ShiftTemplate, on_delete=models.CASCADE)
    volunteer = models.ManyToManyField(Volunteer, through="ShiftVolunteer")


class ShiftVolunteer(models.Model):
    scheduled_shift = models.ForeignKey(ScheduledShift, on_delete=models.CASCADE)
    notes = models.CharField(max_length=100)
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.


class Organization(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=500)
    user = models.ManyToManyField(User)

class Venue(models.Model):
    name = models.CharField(max_length=150)
    location = models.CharField(max_length=500)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Event(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, blank=True, null=True)
    description = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    date = models.DateField(null=True, blank=True)
    sign_up_url = models.CharField(max_length=50, null=True, blank=True, unique=True, default=uuid.uuid4)
    is_template = models.BooleanField()

class Shift(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    num_volunteers = models.PositiveIntegerField()
    description = models.CharField(max_length=100)

    @property
    def slots_remaining(self):
        volunteers = Volunteer.objects.filter(shift=self).count()
        return self.num_volunteers - volunteers

class Volunteer(models.Model):
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, default="volunteer")
    note = models.CharField(max_length=100, null=True, blank=True)




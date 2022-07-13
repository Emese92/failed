from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# maybe not needed
import datetime as dt


class Book(models.Model):
    slug = models.SlugField(max_length=200, unique=True)
    booked_date = models.DateField()
    booked_time = models.TimeField(default=dt.time(00, 00))
    name = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
    party_size = models.PositiveSmallIntegerField(null=False)
    extra_info = models.TextField(blank=True)
    booked_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['booked_date']

    def new_booking(self):
        return self.name

    def confirmation(self):
        return self.approved
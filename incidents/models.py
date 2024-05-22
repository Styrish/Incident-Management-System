from django.db import models
from django.contrib.auth.models import User
import datetime

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    pin_code = models.CharField(max_length=6)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

class Incident(models.Model):
    REPORTER_TYPE_CHOICES = [
        ('Enterprise', 'Enterprise'),
        ('Government', 'Government'),
    ]
    PRIORITY_CHOICES = [
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    ]
    STATUS_CHOICES = [
        ('Open', 'Open'),
        ('In progress', 'In progress'),
        ('Closed', 'Closed'),
    ]

    reporter = models.ForeignKey(User, on_delete=models.CASCADE)
    incident_id = models.CharField(max_length=15, unique=True)
    reporter_type = models.CharField(max_length=10, choices=REPORTER_TYPE_CHOICES)
    details = models.TextField()
    reported_date = models.DateTimeField(default=datetime.datetime.now)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES)
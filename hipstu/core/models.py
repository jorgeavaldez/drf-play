from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Link(models.Model):
    raw_url = models.CharField(max_length=2083)
    affiliate_url = models.CharField(max_length=2083, blank=True)
    #affiliate_url_added_by = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
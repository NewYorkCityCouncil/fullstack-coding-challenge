from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# Create your models here.
class UserProfile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  district_number = models.CharField(max_length=5, blank=True, default="")
  party = models.CharField(max_length=50, blank=True, default="")
  borough = models.CharField(max_length=50, blank=True, default="")
  def __str__(self):
    return str(self.user)
class Complaint(models.Model):
  unique_key = models.CharField(max_length=150, blank=True, default="")
  account = models.CharField(max_length=10, blank=True, default="")
  opendate = models.DateTimeField(blank=True, null=True)
  complaint_type = models.CharField(max_length=150, blank=True, default="")
  descriptor = models.CharField(max_length=150, blank=True, default="")
  zip = models.CharField(max_length=5, blank=True, default="")
  borough = models.CharField(max_length=50, blank=True, default="")
  city = models.CharField(max_length=50, blank=True, default="")
  council_dist = models.CharField(max_length=10, blank=True, default="")
  community_board = models.CharField(max_length=150, blank=True, default="")
  closedate = models.DateTimeField(blank=True, null=True)
  def __str__(self):
    return str(self.unique_key)
from django.contrib import admin
from complaint_app.models import UserProfile, Complaint

# Register your models here.
admin.site.register(Complaint)
admin.site.register(UserProfile)
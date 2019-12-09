from django.contrib.auth.models import User
from .models import UserProfile, Complaint
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username', 'first_name','last_name')

class UserProfileSerializer(serializers.ModelSerializer):
    # BONUS Task: Flatten out the User object inside of UserProfile.
    class Meta:
        model = UserProfile
        fields = ('id','user','full_name','district','party','borough')

class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaint
        fields = ('unique_key','account','opendate','complaint_type','descriptor','zip','borough','city','council_dist','community_board','closedate')
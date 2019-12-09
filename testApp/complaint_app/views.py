from rest_framework import viewsets
from .models import UserProfile, Complaint
from .serializers import UserSerializer, UserProfileSerializer, ComplaintSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class ComplaintViewSet(viewsets.ModelViewSet):
  http_method_names = ['get']
  serializer_class = ComplaintSerializer
  def list(self, request):
    # Get all complaints from the user's district
    return Response()

class OpenCasesViewSet(viewsets.ModelViewSet):
  http_method_names = ['get']
  def list(self, request):
    # Get only the open complaints from the user's district
    return Response()

class ClosedCasesViewSet(viewsets.ModelViewSet):
  http_method_names = ['get'] 
  def list(self, request):
    # Get only complaints that are close from the user's district
    return Response()
    
class TopComplaintTypeViewSet(viewsets.ModelViewSet):
  http_method_names = ['get']
  def list(self, request):
    # Get the top 3 complaint types from the user's district
    return Response()
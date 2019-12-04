from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class ComplaintViewSet(viewsets.ModelViewSet):
  http_method_names = ['get','put','post']

  def list(self, request):
    pass
  def retrieve(self, request, pk=None):
    pass
  def create(self, request):
    pass
class OpenCasesViewSet(viewsets.ModelViewSet):
  http_method_names = []
class ClosedCasesViewSet(viewsets.ModelViewSet):
  http_method_names = []
class TopComplaintTypeViewSet(viewsets.ModelViewSet):
  http_method_names = []
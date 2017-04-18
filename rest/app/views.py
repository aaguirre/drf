import requests

from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import UserSerializer, GroupSerializer


"""
ViewSet from Django REST Framework quickstart tutorial 
"""

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


def index(request):
    """ From Django quickstart tutorial
    """
    return HttpResponse("Hello!")

@api_view()
def sources(request):
    data = requests.get('https://asa.alma.cl/sc/sources/')
    return Response(data.json())

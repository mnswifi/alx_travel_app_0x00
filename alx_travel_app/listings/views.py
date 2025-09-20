from django.shortcuts import render
from rest_framework import viewsets
from .models import Listing
from .serializers import ListingSerializer

# Create your views here.


class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all().order_by('-created_at')
    serializer_class = ListingSerializer

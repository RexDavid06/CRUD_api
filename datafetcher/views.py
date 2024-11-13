from django.shortcuts import render
from .models import Fetch
from .serializers import FetchSerializer
from rest_framework import generics

# Create your views here.
class FetchCreateView(generics.ListCreateAPIView):
    queryset = Fetch.objects.all()
    serializer_class = FetchSerializer


class FetchUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fetch
    serializer_class = FetchSerializer
    lookup_field = 'pk'
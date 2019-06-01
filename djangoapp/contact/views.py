from django.shortcuts import render
from .models import Contact
from rest_framework import viewsets
from .serializers import  ContactSerializer

# Create your views here.
class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


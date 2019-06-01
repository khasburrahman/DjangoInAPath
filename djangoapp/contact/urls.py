from django.urls import path, include
from .views import ContactViewSet
from rest_framework.routers import DefaultRouter

contact_router = DefaultRouter()
contact_router.register(r'contacts', ContactViewSet, basename='contact')

urlpatterns = [
    path('contacts/', include(contact_router.urls))
]
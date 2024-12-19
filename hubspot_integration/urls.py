from django.urls import path
from . import views

urlpatterns = [
    path('deals/', views.get_deals, name='get_deals'),
    path('contacts/', views.get_contacts, name='get_contacts'),
    path('link/', views.associate_deal_contact, name='associate_deal_contact'),
]

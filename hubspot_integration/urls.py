from django.urls import path
from .views import get_deals, get_contacts, LinkDealView

urlpatterns = [
    path('deals/', get_deals, name='get-deals'),
    path('contacts/', get_contacts, name='get-contacts'),
    path('link/', LinkDealView.as_view(), name='link-deal'),
]

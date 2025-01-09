from django.urls import path
from .views import get_deals, get_contacts, LinkObjectsView

urlpatterns = [
    path('deals/', get_deals, name='get-deals'),
    path('contacts/', get_contacts, name='get-contacts'),
    path('link-objects/<str:object_type_from>/<str:object_type_to>/', LinkObjectsView.as_view(), name='link-objects'),
]

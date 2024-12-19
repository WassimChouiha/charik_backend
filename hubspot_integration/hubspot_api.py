import requests
from django.conf import settings

HUBSPOT_BASE_URL = "https://api.hubapi.com"

def fetch_deals():
    url = f"{HUBSPOT_BASE_URL}/deals/v1/deal/paged"
    headers = {
        "Authorization": f"Bearer {settings.HUBSPOT_ACCESS_TOKEN}"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def fetch_contacts():
    url = f"{HUBSPOT_BASE_URL}/contacts/v1/lists/all/contacts/all"
    headers = {
        "Authorization": f"Bearer {settings.HUBSPOT_ACCESS_TOKEN}"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def link_deal_to_contact(deal_id, contact_id):
    url = f"{HUBSPOT_BASE_URL}/crm/v3/objects/deals/{deal_id}/associations/contacts/{contact_id}/HUBSPOT_DEFINED"
    headers = {
        "Authorization": f"Bearer {settings.HUBSPOT_ACCESS_TOKEN}",
        "Content-Type": "application/json",
    }
    response = requests.put(url, headers=headers)
    response.raise_for_status()
    return response.json()

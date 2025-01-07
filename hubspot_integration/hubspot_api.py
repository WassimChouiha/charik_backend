import requests
from requests.exceptions import RequestException
from django.conf import settings
HUBSPOT_BASE_URL = "https://api.hubapi.com"

headers = {
        "Authorization": f"Bearer {settings.HUBSPOT_ACCESS_TOKEN}",
        "Content-Type": "application/json",
    }
def fetch_deals():
    url = f"{HUBSPOT_BASE_URL}/deals/v1/deal/paged"
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except RequestException as e:
        # Log or handle the error as appropriate
        raise Exception(f"Error fetching deals: {str(e)}")

def fetch_contacts():
    url = f"{HUBSPOT_BASE_URL}/contacts/v1/lists/all/contacts/all"
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except RequestException as e:
        raise Exception(f"Error fetching contacts: {str(e)}")

def link_deal_to_contact(deal_id, contact_id):
    url = f"{HUBSPOT_BASE_URL}/crm/v3/objects/contacts/{contact_id}/associations/0-3/{deal_id}/4"
    
    
    try:
        response = requests.put(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except RequestException as e:
        raise Exception(f"Error linking deal to contact: {str(e)}")

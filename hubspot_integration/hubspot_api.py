import requests
from requests.exceptions import RequestException
from django.conf import settings
HUBSPOT_BASE_URL = "https://api.hubapi.com"

headers = {
        "Authorization": f"Bearer {settings.HUBSPOT_ACCESS_TOKEN}",
        "Content-Type": "application/json",
    }
def fetch_deals():
    url = f"{HUBSPOT_BASE_URL}/crm/v3/objects/deals?limit=100"
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except RequestException as e:
        # Log or handle the error as appropriate
        raise Exception(f"Error fetching deals: {str(e)}")

def fetch_contacts():
    url = f"{HUBSPOT_BASE_URL}/crm/v3/objects/contacts?limit=100"
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except RequestException as e:
        raise Exception(f"Error fetching contacts: {str(e)}")

def link_objects(object_type_from, object_type_to, inputs):
    url = f"{HUBSPOT_BASE_URL}/crm/v4/associations/{object_type_from}/{object_type_to}/batch/associate/default"
    payload = {
                "inputs": inputs
            }
    try:
        response = requests.post(url, headers=headers,json=payload)
        response.raise_for_status()
        return response.json()
    except RequestException as e:
        raise Exception(f"Error linking {object_type_from} to {object_type_to}: {str(e)}")

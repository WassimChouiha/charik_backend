from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .hubspot_api import fetch_deals, fetch_contacts, link_deal_to_contact
from django.http import JsonResponse
import logging

logger = logging.getLogger(__name__)

@api_view(['GET'])
def get_deals(request):
    try:
        deals = fetch_deals()
        return Response(deals, status=status.HTTP_200_OK)
    except Exception as e:
        logger.error(f"Error fetching deals: {e}", exc_info=True)
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def get_contacts(request):
    try:
        contacts = fetch_contacts()
        return Response(contacts, status=status.HTTP_200_OK)
    except Exception as e:
        logger.error(f"Error fetching contacts: {e}", exc_info=True)
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class LinkDealView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            deal_id = request.data.get("deal_id")
            contact_id = request.data.get("contact_id")
            if not deal_id or not contact_id:
                return Response({"error": "Missing deal_id or contact_id"}, status=status.HTTP_400_BAD_REQUEST)
            
            response = link_deal_to_contact(deal_id, contact_id)
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Error linking deal and contact: {e}", exc_info=True)
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def my_view(request):
    try:
        result = 1 / 0  
        return JsonResponse({'result': result})
    except ZeroDivisionError as e:
        logger.error(f"An error occurred: {e}", exc_info=True)
        return JsonResponse({'error': 'An internal error occurred'}, status=500)

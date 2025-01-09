from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .hubspot_api import fetch_deals, fetch_contacts, link_objects
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

class LinkObjectsView(APIView):
    def post(self, request, object_type_from, object_type_to, *args, **kwargs):
        try:
            # Validate that the request body is a list
            link_data = request.data
            if not isinstance(link_data, list):
                return Response(
                    {"error": "Expected a list of objects to link"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            # Prepare the inputs for the HubSpot API
            inputs = []
            for link in link_data:
                from_id = link.get("from_id")
                to_id = link.get("to_id")
                
                if not from_id or not to_id:
                    return Response(
                        {"error": "Missing from_id or to_id in one of the objects"},
                        status=status.HTTP_400_BAD_REQUEST
                    )
                
                # Prepare the input format for each association
                inputs.append({
                    "from": {"id": from_id},
                    "to": {"id": to_id}
                })
            
            response = link_objects(object_type_from, object_type_to, inputs)
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Error linking {object_type_from} and {object_type_to}: {e}", exc_info=True)
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
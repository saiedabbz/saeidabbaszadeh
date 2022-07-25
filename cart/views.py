from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from hq.io import response

from .services import load_cart, cart_item_amount, append_cart_items


@csrf_exempt
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def cart(request):
    return response({
        "cart": load_cart(request.user),
    })


@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def set_cart_item(request):
    '''
    {
        variant_id: int
        amount: int
    }
    '''
    data = request.data

    return response({
        "item_amount": cart_item_amount(request.user, data["variant_id"], data.get('amount', 1)),
    })



@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def set_cart_items(request):
    return response({"cart": append_cart_items(request.user, request.data['items'])})
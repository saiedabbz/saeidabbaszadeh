from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from hq.io import response

from .services import init_order, order_address, order_datetime, payment, load_order, load_orders


@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_order(request):
    return response({"order": init_order(request.user)})


@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_address(request):
    return response({"order": order_address(request.user, request.data.pop("order_id"), request.data)})


@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_datetime(request):
    return response({"order": order_datetime(request.user, request.data.pop("order_id"), request.data)})


@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def finalize_order(request):
    return response({"order": payment(request.user, request.data.get("order_id"))})


@csrf_exempt
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def load_one_order(request, pk):
    return response({"order": load_order(request.user, pk)})


@csrf_exempt
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def load_many_orders(request):
    return response({"order": load_orders(request.user, {**request.query_params})})
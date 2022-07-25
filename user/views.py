from rest_framework_simplejwt.views import TokenViewBase
from .serializers import TokenObtainLifetimeSerializer, TokenRefreshLifetimeSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from hq.io import response
from .services import addresses, edit_address, edit_user, create_user, create_address, load_address, load_user

class TokenObtainPairView(TokenViewBase):
    """
        Return JWT tokens (access and refresh) for specific user based on username and password.
    """
    serializer_class = TokenObtainLifetimeSerializer


class TokenRefreshView(TokenViewBase):
    """
        Renew tokens (access and refresh) with new expire time based on specific user's access token.
    """
    serializer_class = TokenRefreshLifetimeSerializer


@csrf_exempt
@api_view(['POST'])
def signup(request):
    return create_user(request.data)
    


@csrf_exempt
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def load_addresses(request):
    return response({"addresses": addresses({"user": request.user})})


@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_address(request):
    return response({"address": create_address(request.user, request.data)})


class UserAPI(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return response({"user": load_user(request.user)})

    def put(self, request):
        return response({"user": edit_user(request.user, request.data)})


class AddressAPI(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, pk):
        return response({"user": load_address({"user":request.user, "id": pk})})

    def put(self, request, pk):
        return response({"user": edit_address({"user":request.user, "id": pk}, request.data)})
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from .models import Customer
from .serializers import CustomerSerializer

class CustomerListApiView(APIView):
    permissions_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        customer = Customer.objects.all()
        serialize = CustomerSerializer(customer, many=True)

        return Response(serialize.data, status=status.HTTP_200_OK)


    def post(self, request, *args, **kwargs):

        data = {
            'name': request.data.get('name'),
            'date_joined': request.data.get('date_joined'),
        }
        serialize = CustomerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

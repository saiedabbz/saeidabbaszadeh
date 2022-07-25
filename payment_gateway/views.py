from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view


@csrf_exempt
@api_view(['GET', 'POST'])
def bank_callback(request, transaction_id):
    pass


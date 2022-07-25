from django.core.exceptions import PermissionDenied
from django.http import Http404

from rest_framework.response import Response
from rest_framework.views import set_rollback
from rest_framework import exceptions
from pydantic import ValidationError
import traceback

def response(data: dict, message: str = '', success: bool = True, status: int = 200):
    return Response({
        'data': data,
        'message': message,
        'success': success
    }, status)


def internal_exception_handler(exc, context):
    traceback.print_exc()
    if isinstance(exc, Http404):
        exc = exceptions.NotFound()
    elif isinstance(exc, PermissionDenied):
        exc = exceptions.PermissionDenied()

    data = {}
    message =  f'internal error: {str(exc)}'
    status = 500

    if isinstance(exc, exceptions.APIException):
        headers = {}
        if getattr(exc, 'auth_header', None):
            headers['WWW-Authenticate'] = exc.auth_header
        if getattr(exc, 'wait', None):
            headers['Retry-After'] = '%d' % exc.wait

        if isinstance(exc.detail, (list, dict)):
            data = {'errors': exc.detail}
            message = 'check data.errors for detail'
        else:
            message =  exc.detail

        status = exc.status_code
        set_rollback()

    
    if isinstance(exc, ValidationError):
        data = {'errors': exc.errors()}
        message = 'check data.errors for detail'
        status = 422


    return response(data, message, False, status)




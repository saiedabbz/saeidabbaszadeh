from .models import User, UserAddress
from .serializers import UserAddressManySerializer, UserAddressOneSerializer, UserSerializer
from .utils import UserQueryBuilder, AddressQueryBuilder
from django.http import Http404
from rest_framework_simplejwt.tokens import RefreshToken, SlidingToken, UntypedToken
from hq.io import response


def addresses(filter: dict):
    build = AddressQueryBuilder(filter)
    addr = UserAddress.objects.filter(**build.query).order_by(build.sort_by)
    return UserAddressManySerializer(addr, many=True).data


def load_address(filter: dict):
    build = AddressQueryBuilder(filter)
    if not UserAddress.objects.filter(**build.query).exists():
        raise Http404

    addr = UserAddress.objects.get(**build.query)
    return UserAddressOneSerializer(addr).data


def edit_address(filter: dict, data: dict):
    build = AddressQueryBuilder(filter)
    if not UserAddress.objects.filter(**build.query).exists():
        raise Http404

    addr = UserAddress.objects.get(**build.query)

    addr.title = data.get('title', addr.title)
    addr.state = data.get('state', addr.state)
    addr.city = data.get('city', addr.city)
    addr.addr = data.get('addr', addr.addr)
    addr.postal_code = data.get('postal_code', addr.postal_code)
    addr.national_code = data.get('national_code', addr.national_code)
    addr.full_name = data.get('full_name', addr.full_name)
    addr.mobile = data.get('mobile', addr.mobile)
    addr.save()

    return UserAddressOneSerializer(addr).data


def load_user(user: User):
    return UserSerializer(user).data


def edit_user(user: User, data: dict):
    user.first_name = data.get('first_name', user.first_name)
    user.last_name = data.get('last_name', user.last_name)
    user.save()

    return UserSerializer(user).data


def create_user(data: dict):
    if User.objects.filter(username=data['username']).exists():
        return response({}, 'username exists', False, 422)

    if data['password'] != data['password_confirm']:
         return response({}, "password doesn't match", False, 422)

    user = User.objects.create(
        username=data['username']
    )

    user.set_password(data['password'])


    SlidingToken.for_user(user)
    RefreshToken.for_user(user)
    str(RefreshToken.for_user(user))
    str(RefreshToken.for_user(user).access_token)

    return response({
        "user": UserSerializer(user).data, 
        "access": str(RefreshToken.for_user(user).access_token),
        "refresh": str(RefreshToken.for_user(user).access_token)
    })


def create_address(user: User, data: dict):
    addr = UserAddress.objects.create(
        user=user,
        title=data['title'],
        state=data['state'],
        city=data['city'],
        addr=data['addr'],
        postal_code=data['postal_code'],
        national_code=data['national_code'],
        full_name=data['full_name'],
        mobile=data['mobile']
    )

    return UserAddressOneSerializer(addr).data


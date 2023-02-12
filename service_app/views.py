from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

from service_app.models import Valentine, User
from service_app.serializers import ValentineSerializer, UserSerializer


@api_view(["GET"])
def health_check(request):
    return Response({"status": "Ok"}, status.HTTP_200_OK)


class ValentineRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = Valentine.objects.all()
    serializer_class = ValentineSerializer


class ValentineList(generics.ListCreateAPIView):
    queryset = Valentine.objects.all()
    serializer_class = ValentineSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['sender', 'recipient', 'status']


class UserRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = Valentine.objects.all()
    serializer_class = ValentineSerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['telegram_id', 'username']





# class ValentinePaginationList(generics.ListCreateAPIView):
#     queryset = Valentine.objects.all()
#     serializer_class = ValentineSerializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['sender', 'recipient', 'status']

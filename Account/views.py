from django.shortcuts import render
from rest_framework import viewsets
from Account.serializers import AccountModelSerializers
from Account.models import Account
# Create your views here.

class AccountModelViewset(viewsets.ModelViewSet):
    serializer_class = AccountModelSerializers
    queryset = Account.objects.all()


from rest_framework import serializers
from Account.models import Account

class AccountModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"
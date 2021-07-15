from rest_framework import fields, serializers
from transaction import models as txnmodels

class transactionserializer(serializers.ModelSerializer):
    class Meta:
        model = txnmodels.transaction_model 
        fields = "__all__"


class reward_modelserializer(serializers.ModelSerializer):
    class Meta:
        model = txnmodels.reward_model
        fields = "__all__"
from django.db import models
from django.db.models import fields
from rest_framework import serializers
from rest_framework.utils import field_mapping
from customer.models import user_profile
# from customer.models import 

class user_profile_serializer(serializers.ModelSerializer):
    class Meta:
        model = user_profile
        # fields = ["user_name","user_type","is_agent","user_phone","user_email","is_verified"]
        fields = "__all__"
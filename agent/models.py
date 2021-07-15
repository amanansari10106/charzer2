# from organization.models import organization
from django.db.models.deletion import CASCADE
from customer.models import user_profile
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class agent(models.Model):
    # agent = models.OneToOneField(User,on_delete=CASCADE, primary_key=True)
    agent_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    service_provider = models.CharField(max_length=30, null=True)
    balance_amount = models.FloatField(default=0)
    bank_acc_no = models.CharField(max_length=50)
    bank_name = models.CharField(max_length=30)
    bank_acc_name = models.CharField(max_length=50)
    bank_ifsc = models.CharField(max_length=20)
    agent_is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# class org_agent(models.Model):
#     org_agent_id = models.AutoField(primary_key=True)
#     user = models.OneToOneField(User,on_delete=models.CASCADE)
#     org = models.ForeignKey(organization, on_delete=models.CASCADE)
    # supervisor = models.ForeignKey(supervsor_model, on_delete=models.CASCADE)

# class new_agent(models.Model):
#     agent = models.OneToOneField(User,on_delete=CASCADE, primary_key=True)
#     # user_id = models.ForeignKey(user_profile)
#     # service_provider = models.CharField(max_length=30)
#     # bank_acc_no = models.CharField(max_length=50)
#     # bank_name = models.CharField(max_length=30)
#     # bank_acc_name = models.CharField(max_length=50)
#     # bank_ifsc = models.CharField(max_length=20)
#     activation_status = models.BooleanField(default=False)
#     balance_amount = models.FloatField(null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

# class new_org_agent(models.Model):
#     org_agent = models.OneToOneField(agent, on_delete=models.CASCADE)
#     organization = models.ForeignKey(organization, on_delete=models.CASCADE)
#     month_money_earned = models.FloatField()
#     total_money_earned = models.FloatField()



# class normal_agent(models.Model):
#     bank_acc_no = models.CharField(max_length=50)
#     bank_name = models.CharField(max_length=30)
#     bank_acc_name = models.CharField(max_length=50)
#     bank_ifsc = models.CharField(max_length=20)
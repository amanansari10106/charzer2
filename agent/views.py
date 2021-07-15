from functools import partial
from django.shortcuts import render
from rest_framework import serializers

# Create your views here.

from rest_framework.serializers import Serializer
from rest_framework.utils import serializer_helpers
# from customer.serializers import user_profile_serializer
from customer.models import user_profile
from django.core.checks.messages import Error
from django.http.response import HttpResponse
from django.shortcuts import render
import django.contrib.auth
# User = django.contrib.auth.get_user_model()
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
# user = User.objects.create_user('username', password='userpassword')
# user.is_superuser = False
# user.is_staff = False
# user.save()
# Create your views here.
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

from agent.models import agent
from agent.serializers import agentserializer, agentserialzerupdate


class becomeAgent(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes  = [IsAuthenticated]
    def post(self, request):
        
        try :
            print("#################################")
            user = user_profile.objects.get(user=request.user)
            if user.is_verified and user.user_type=="customer":
                data = request.data
                print("11")
                a = agent(user=request.user,service_provider=data["service_provider"], bank_acc_no=data["bank_acc_no"], bank_name=data["bank_name"],bank_acc_name=data["bank_acc_name"],bank_ifsc=data["bank_ifsc"])
                a.save()
                a.agent_is_active = True
                # user.update(user_type="agent")
                user.user_type = "agent"
                user.save()
                msg = {
                    "msg":"you are now a agent",
                    "res": "successful"
                }
                serializer = agentserialzer(a)
                msg.update(serializer.data)
                return Response(msg, status=status.HTTP_200_OK)
            else:
                print("4")
                msg = {
                    "msg":f"You are already a {user.user_type} or Your user id is not verified",
                    "res":"fail"
                }
                return Response(msg, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            msg ={
                "resp":"hel"
            }
            return Response(msg, status=status.HTTP_400_BAD_REQUEST)

    # def get(self, request):
    #     user = user_profile.objects.get(user=request.user)
    #     # user.update(user_type="agent")
    #     user.user_type = "agent"
    #     user.save()
    #     return Response({"msg":"done"})

class agentdetail(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes  = [IsAuthenticated]
    def get(sel, request):
        try : 
            # user = user_profile.objects.get(user=request.user)
            # if user.user_type == "agent":
            # print("############")
            ag = agent.objects.get(user=request.user)
            # print(ag)
            serializer = agentserialzer(ag)
            return Response(serializer.data, status=status.HTTP_200_OK)
            
        except Exception as e:
            # print(e)
            return Response({"msg":f"{e}"}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        try :
            ag = agent.objects.get(user=request.user)
            serializer = agentserialzerupdate(ag, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                ag = agent.objects.get(user=request.user)
                se = agentserializer(ag)
                return Response(serializer.data, status=status.HTTP_200_OK)

            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        except Exception as e:
            return Response({"msg":f"{e}"}, status=status.HTTP_400_BAD_REQUEST)
            

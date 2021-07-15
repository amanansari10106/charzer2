from charzer import settings
from customer.serializers import user_profile_serializer
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
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token




class user_register(APIView):

    def get(self, request):
        username = request.data.get('username')
        if User.objects.filter(username=username).exists():

            msg = {
                "msg": "username-not-available",
                "resp":"stop"
            }
            return Response(msg)
            pass
        else:
            msg = {
                "msg": "username-available",
                "resp":"proceed"
            }

            return Response(msg)


    def post(self,request):
        gusername = request.data.get('username')
        if User.objects.filter(username=gusername).exists():
            msg = {
                "msg": "not-available",
                "resp":"username-not-available"
            }

            return Response(msg)

        else:
            username = request.data.get('username')
            password = request.data.get('password')

            try:
                user = User.objects.create_user(username, password=password)
                user.is_superuser = False
                user.is_staff = False
                user.save()
                u = user_profile(user=user, user_name=user.username)
                u.save()

                # print(token.key)
            except Exception as e:
                return Response({"msg":f"{e}","resp":"fail"})
            token = Token.objects.create(user=user)
            # print(token)
            # print(type(token))
            return Response({"msg":"created user successfully","resp":"successful","token": str(token)})


class user_profile_api(APIView):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes  = [IsAuthenticated]

    # def get(self, request):
    #     u = user_profile.objects.get(user=request.user)

    #     serializer = user_profile_serializer(u)
    #     return Response(serializer.data)

    def get(self, request):
        try :
            u = user_profile.objects.get(user=request.user)
            serializer = user_profile_serializer(u)
            dat = serializer.data
            dat["user_photo"] = settings.website_name + dat["user_photo"]
            return Response(dat, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(serializer.errors, status=status)
    def post(self, request):
        if "is_verified" in request.data or "user_credit" in request.data:
            return Response({"resp":"bad request"}, status=status.HTTP_400_BAD_REQUEST)
        user = user_profile.objects.get(user=request.user)
        serializer = user_profile_serializer(user,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# from django.http import JsonResponse
# class user_login(APIView):
#     authentication_classes = [TokenAuthentication]
#     permission_classes  = [IsAuthenticated]

#     def get(self, request):
#         # username = request.data.get('username')
#         # password = request.data.get('password')
#         msg = {
#             "hello":"world"
#         }
#         # return HttpResponse('{"hello":"world"',content_ty)
#         return Response(msg)

# from rest_framework.decorators import api_view

# @api_view()
# def temp(request):
#     u = user_profile.objects.all()
#     st = user_profile_serializer(u)
#     return Response(st.data)
# class gettokenz(APIView):
#     authentication_classes = [TokenAuthentication]
#     permission_classes  = [IsAuthenticated]
#     def get(self, request):
#         a = request.user
#         z = user_profile(user=a, user_name=a.username)
    
#         return HttpResponse(z)

        
        
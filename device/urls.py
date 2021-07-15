# from rest_framework import views
# from device.models import device
from device.views import deviceapi, near
from device import views
from django.urls import path

urlpatterns = [
    path("api/",deviceapi.as_view()),
    path("neardevice/", near.as_view()),
    path("tes/", views.test)
]
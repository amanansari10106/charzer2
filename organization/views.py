from django.shortcuts import render
from rest_framework.views import APIView
from django.shortcuts import render
# Create your views here.

class orgregister(APIView):

    def get(self, request):
        return render(request, "org/org_register.html")
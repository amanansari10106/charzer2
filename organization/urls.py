from django.urls import path
from django.urls.resolvers import URLPattern
from organization import views
urlpatterns =[
    path("register",views.orgregister.as_view())
]
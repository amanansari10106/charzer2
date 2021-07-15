from django.urls.conf import path
from transaction import views
urlpatterns = [
    path("api/",views.transactionapi.as_view()),
    path("reward/",views.reward.as_view()),
    path("addmoney/",views.addmoney.as_view()),
    path("verifyaddmoney/", views.verifyaddmoney.as_view())
]

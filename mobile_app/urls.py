from django.conf.urls import url
from .views import getCash,sendDataToHost,homePage


urlpatterns=[
    url(r'home$',homePage,name='app_home'),
    url(r'withdraw_to_app$',sendDataToHost,name="withdraw_to_app"),
    url(r'get_cash$',getCash,name="get_cash")
]
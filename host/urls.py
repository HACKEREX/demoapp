from django.conf.urls import url
from .views import withdrawFun,withdrawMob,withdrawCash


urlpatterns = [
    url(r'withdraw/(?P<encrypted_data>\.*)$',withdrawFun,name='withdraw_fun'),
    url(r'withdrawmob/',withdrawMob,name="withdraw_mob"),
    url(r'withdraw_cash',withdrawCash,name="withdraw_cash")
]

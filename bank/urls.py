from django.conf.urls import url
from .views import withdrawMoneyViaAtm

urlpatterns=[
    url(r'transaction/withdraw/(?P<encrypted_data>.*)/$', withdrawMoneyViaAtm,name='withdraw_from_bank')
]
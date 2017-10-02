from django.conf.urls import url,include
from .views import AtmHome,AtmTransactionResult,DispenseCash

urlpatterns=[
    url(r'home$',AtmHome,name="atm_home"),
    url(r'transaction/withdraw',AtmTransactionResult,name="atm_transaction_result"),
    url(r'dispense_cash/(?P<atm_id>.*)/(?P<transaction_id>.*)/$',DispenseCash,name="dispense_cash")
]
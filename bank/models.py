from __future__ import unicode_literals

from django.db import models
from django.core.validators import RegexValidator


BANK_NAMES=[
    ('1','SBI'),
    ('2','AXIS BANK'),
    ('3','BANK OF INDIA'),
]

ACCOUNT_STATUS=[
    ('1','ACTIVE'),
    ('2','DORMANT')
]

ERRORCODES=[
    "Transaction Successful",
    "Account Does Not Exist",
    "Account Currently Not Active",
    "Current Amount Unable to Dispense"
]

class BankUser(models.Model):

    bank_name=models.CharField(choices=BANK_NAMES,default=1,blank=False,max_length=50)
    account_no=models.CharField(max_length=11,blank=False)
    account_type=models.CharField(choices=[('1','SAVINGS'),('2','CURRENT')],default='1',blank=False,max_length=30)
    card_no=models.CommaSeparatedIntegerField(max_length=16,validators=[RegexValidator(r'\d\d\d\d')])
    registered_mob_no=models.CharField(max_length=13,blank=False)
    current_balance=models.CharField(max_length=20,default=1000,blank=False)
    account_status=models.CharField(choices=ACCOUNT_STATUS,default='1',blank=False,max_length=20)


    def __str__(self):
        return self.account_no


class Bank(models.Model):

    name=models.CharField(choices=BANK_NAMES,default=1,blank=False,max_length=50)
    address=models.TextField(max_length=150)
    ifsc=models.CharField(max_length=20)

    def __str__(self):
        return self.ifsc



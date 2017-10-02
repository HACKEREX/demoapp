from __future__ import unicode_literals

from django.db import models
from bank.models import BankUser
import django.utils


TRANSACTION_TYPE=[
    ('1','WITHDRAW'),
    ('2','CREDIT'),
    ('3','TRANSFER')
]

TRANSACTION_STATUS=[
    ('1','PENDING'),
    ('2','COMPLETED')
]


class AppUser(models.Model):
    user_added=models.DateTimeField(auto_now_add=True)
    google_play_account=models.URLField(max_length=128,blank=False)
    user_name=models.CharField(max_length=150,blank=False)
    account_password=models.CharField(max_length=128)


    class Meta:
        ordering=('google_play_account',)


    def __str__(self):
        return self.google_play_account


class BankDetails(models.Model):
    registered_ph_no = models.CharField(max_length=13, blank=False)
    registered_account = models.OneToOneField(BankUser,unique=True,on_delete=models.CASCADE)
    registered_user = models.OneToOneField(AppUser,unique=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.registered_user.google_play_account + "( "+self.registered_account.account_no+" )"



class Transaction(models.Model):

    transaction_started_at=models.DateTimeField(auto_created=True)
    transaction_ended_at=models.DateTimeField(auto_created=True)
    transaction_account=models.CharField(max_length=11,blank=False,default=1)
    transaction_type=models.CharField(max_length=20,choices=TRANSACTION_TYPE,blank=False,default='1')
    transaction_id=models.CharField(max_length=150,blank=False,default="TRAN" + "TM"+str(id))
    transaction_amount=models.CharField(max_length=30,default=0,blank=False)
    transaction_withdrawl=models.CharField(choices=TRANSACTION_STATUS,default='1',blank=False,max_length=20)

    def __str__(self):
        return self.transaction_id

    def save(self, *args,**kwargs):

        if not self.id:
            self.transaction_started_at=django.utils.timezone.now()
            self.transaction_id="TRAN"+self.transaction_account+\
                                "TM"+str(self.transaction_started_at)+\
                                "TY"+self.transaction_type

        self.transaction_ended_at=django.utils.timezone.now()

        return super(Transaction,self).save(*args,**kwargs)



from __future__ import unicode_literals

from django.db import models
from bank.models import Bank



class ATMMachine(models.Model):
    current_amount=models.IntegerField(default=100000)
    address=models.TextField(max_length=500,blank=False,default='Enter ATM ADDRESS HERE')

    bank=models.ForeignKey(Bank,default=1)


    def __str__(self):
        return str(self.bank.ifsc+"__"+str(self.id))


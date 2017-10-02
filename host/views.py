from bank.views import withdrawMoneyViaAtm
import ast
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from mobile_app.models import Transaction
from django.http import JsonResponse,HttpResponse
from django.utils import timezone

def withdrawCash(request):

    if request.method=='POST':
        print(request.POST)
        return redirect(reverse('dispense_cash' ,args=(request.POST["atm_id"],request.POST["transaction_id"])))
    else:
        return HttpResponse("NOT SUPPORTED")



def withdrawFun(request):

    account_no=request.POST['acc_no']
    amount=request.POST['amt']
    csrftoken=request.POST['csrfmiddlewaretoken']

    encrypted_data={"account_no": account_no, "amount": amount, "csrfmiddlewaretoken": csrftoken}
    return withdrawMoneyViaAtm(request,str(encrypted_data) )



def withdrawMob(request):

    account_no = request.POST["acc_no"]
    amount = request.POST["amt"]

    newTran = Transaction.objects.create(transaction_account=account_no, transaction_type='1',transaction_amount=amount)
    newTran.save()



    data_from_bank=withdrawFun(request)

    transaction_info={"account_no":account_no,"amount":amount}
    data_dictionary=ast.literal_eval(data_from_bank.content)

    if data_dictionary["status"]==200:
        data_dictionary["transaction_info"]=transaction_info
        newTran.transaction_ended_at=timezone.now()
        newTran.save()
    else:
        newTran.delete()


    return JsonResponse({"transactionId":newTran.transaction_id,"data_from_host":data_dictionary })

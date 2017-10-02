from django.shortcuts import render,render_to_response,redirect
from django.http import JsonResponse,HttpResponse
from .models import ATMMachine
from host.views import withdrawFun
from mobile_app.models import Transaction
import ast



def AtmHome(request):

    atm_option=ATMMachine.objects.all()
    return render(request,'atm_entry_file.html',{'atm_option':atm_option})



def DispenseCash(request,atm_id,transaction_id):

    atm_info = atm_id.split("__")
    transaction_info=Transaction.objects.get(transaction_id=transaction_id)
    amount=transaction_info.transaction_amount

    atm_in_process = ATMMachine.objects.filter(bank__ifsc=atm_info[0]).filter(id=int(atm_info[1]))

    atm_in_process = atm_in_process[0]

    print(transaction_info)
    print (transaction_info.transaction_amount)


    if (atm_in_process.current_amount - int(amount) < 0):
        return HttpResponse("Unable To Dispense, Notes Not Available")
    else:

        if transaction_info.transaction_withdrawl=='2':
            print("Transaction Already Completed")

        atm_in_process.current_amount-=int(amount)
        atm_in_process.save()
        transaction_info.transaction_withdrawl='2'
        transaction_info.save()

    return HttpResponse("APPROVED")




def AtmTransactionResult(request):


    if request.method=='POST':

        amount = request.POST['amt']
        withdraw_from_atm=request.POST['atm']


        atm_info=withdraw_from_atm.split("__")


        atm_in_process=ATMMachine.objects.filter(bank__ifsc=atm_info[0]).filter(id=int(atm_info[1]))

        atm_in_process=atm_in_process[0]

        if(atm_in_process.current_amount-int(amount)<0):
            return HttpResponse("Unable To Dispense, Notes Not Available")

        responseData=withdrawFun(request)


        returned_data=ast.literal_eval(responseData.content)
        print(type(returned_data))

        if(int(returned_data["status"])==200):
            atm_in_process.current_amount -= int(amount)

            print(atm_in_process.current_amount)
            atm_in_process.save()

        return responseData

    else:
        return render(request,'atm_transaction_result')

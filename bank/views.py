from django.http import HttpResponse,JsonResponse
import ast
from .models import BankUser,ERRORCODES
from rest_framework import status


def withdrawMoneyViaAtm(request,encrypted_data):



    data_dictionary=ast.literal_eval(encrypted_data)

    response_data={"status":200,"responseText":ERRORCODES[0],"errors":0};

    account_no=data_dictionary['account_no']
    amount=data_dictionary['amount']

    print(request.POST['atm'])

    response_data['atm']=request.POST["atm"]


    account_info=BankUser.objects.filter(account_no=account_no)

    if(len(account_info)==0):
        response_data["status"]=404
        response_data["responseText"]=ERRORCODES[1]
        response_data["errors"]=1;


    elif len(account_info)>1:
        response_data["status"] = 403
        response_data["responseText"] = ERRORCODES[1]
        response_data["errors"] = 1;

    else:
        print("Processing Transaction...\n")
        print("Withdrawing....\n")

        account_info=account_info[0]

        if int(account_info.account_status)!=1:
            response_data["status"] = 403
            response_data["responseText"] = ERRORCODES[2]
            response_data["errors"] = 2;


        else:
            if int(account_info.current_balance)<int(amount):

                print(amount)
                print(account_info.current_balance)

                response_data["status"] = 403
                response_data["responseText"] = ERRORCODES[3]
                response_data["errors"] = 3;


            else:
                response_data["status"] = 200
                response_data["responseText"] = ERRORCODES[0]
                response_data["errors"] = 0;

                account_in_current_transaction=BankUser.objects.get(id=account_info.id)
                current_balance=int(account_in_current_transaction.current_balance)
                current_balance-=int(amount)
                account_in_current_transaction.current_balance=current_balance
                account_in_current_transaction.save()


    return JsonResponse(response_data,status=status.HTTP_200_OK)

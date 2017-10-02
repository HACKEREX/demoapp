from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from .models import AppUser
from .serializers import AppUserSerializer
from host.views import withdrawMob
from atm.models import ATMMachine
from django.shortcuts import render
import ast

def user_data(request):
    """List User Data That is in Database"""

    if request.method=='GET':
        all_users=AppUser.objects.all()
        serializer=AppUserSerializer(all_users,many=True)
        return JsonResponse(serializer.data,safe=False)

    elif request.method=='POST':
        data=JSONParser().parse(request)
        serializer=AppUserSerializer(data=data)

        if(serializer.is_valid()):
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,status=400)



def sendDataToHost(request):

    if(request.method=='POST'):
        transaction_id_from_host=withdrawMob(request)
        data_from_host=ast.literal_eval(transaction_id_from_host.content)
        data_from_host["proceed"]=False

        print(data_from_host)

        return render(request,'after_transaction_success.html',{"data_from_host":data_from_host})
    else:
        return HttpResponse("FORBIDDEN")



def getCash(request):
    return HttpResponse("DONE")


def homePage(request):

    atm_option = ATMMachine.objects.all()
    return render(request, 'mobile_index.html', {'atm_option': atm_option})


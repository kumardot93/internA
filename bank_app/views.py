from .models import Bank, BankSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(('GET',))
def BranchAutoComplete(request):
    query_string = request.GET['q']
    offset = 0
    if('offset' in request.GET):
        offset = int(request.GET['offset'])
    bankList = Bank.objects.filter(branch__istartswith=query_string).order_by('ifsc')[offset:]
    if('limit' in request.GET):
        limit = int(request.GET['limit'])
        bankList = bankList[:limit]
    data = BankSerializer(bankList, many=True).data
    return Response({"branches": data})


@api_view(('GET',))
def AutoComplete(request):
    query_string = request.GET['q']
    offset = 0
    if('offset' in request.GET):
        offset = int(request.GET['offset'])
    bankList = Bank.objects.none()
    for fields in Bank._meta.concrete_fields[1:]:
        filterVar = {fields.name+"__istartswith": query_string}
        bankList = bankList | Bank.objects.filter(**filterVar)
    bankList = bankList.order_by('ifsc')[offset:]
    if('limit' in request.GET):
        limit = int(request.GET['limit'])
        bankList = bankList[:limit]
    data = BankSerializer(bankList, many=True).data
    return Response({"branches": data})

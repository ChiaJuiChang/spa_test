from django.shortcuts import render
from django.core import serializers
from .models import Data
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
# Create your views here.
def get_api(request):
    res = serializers.serialize("json", Data.objects.all(),fields=('name', 'pub_date'))
    return HttpResponse(res, content_type="application/json")
    # res = Data.objects.all()
    # res_list = list(res)
    # return JsonResponse(res_list, safe=False)

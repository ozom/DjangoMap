from django.shortcuts import render
from .models import Address
from django.http import HttpResponse
from django.views.generic import View


class index(View):

    def get(self, request, *args, **kwargs):
        address_list = Address.objects.all()
        context = {
            'address_list': address_list,
        }
        return render(request, 'map/index.html', context)

    def post(self, request, *args, **kwargs):
        a = Address.objects.create(address = request.POST['address'], longitude=request.POST['longitude'], latitude=request.POST['longitude'])
        return HttpResponse(a)
 

from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from new_gsgui import settings
from rest_framework import viewsets
from django.contrib.auth.decorators import login_required

from logger.models import *
from logger.serializers import *

def Login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request,'logger/index.html')
            else:
                return HttpResponse("Inactive user.")
        else:
            return HttpResponseRedirect(settings.LOGIN_URL)

    return render(request, "logger/login.html")
@login_required
def Logout(request):
	logout(request)
	return HttpResponseRedirect(settings.LOGIN_URL)

class BMSViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BMSData.objects.all()
    serializer_class = BMSSerializer
class MCViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MCData.objects.all()
    serializer_class = MCSerializer
class MotorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MotorData.objects.all()
    serializer_class = MotorSerializer
class GeneralViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = GeneralData.objects.all()
    serializer_class = GeneralSerializer
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serilizer import Userserializer,Registerserializer
from rest_framework import status
from .models import User
# Create your views here.

@api_view(['POST'])
def createuser(request):    
    if request.method=="POST":
        newuser=Registerserializer(data=request.data)
        if newuser.is_valid():
            newuser.save()
            return Response(newuser.data,status=status.HTTP_200_OK)
        return Response(newuser.errors,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    Response(request,status=status.HTTP_406_NOT_ACCEPTABLE)


@api_view(["GET"])
def getuser(request):
    if request.method=="GET":
        user=User.objects.all()
        userobj=Userserializer(user,many=True)
        return Response(userobj.data)
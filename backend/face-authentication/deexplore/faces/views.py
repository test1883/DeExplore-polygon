from django.shortcuts import render
from rest_framework.views import APIView
from . models import *
from rest_framework.response import Response
from . serializer import *
from rest_framework.parsers import MultiPartParser, FormParser


# Create your views here.

class AddView(APIView):
    serializer_class = ReactSerializer
    parser_classes = (MultiPartParser, FormParser)
    def get(self, request):
        detail = [ {"name": detail.name,"address": detail.address, "username": detail.username}
		for detail in React.objects.all()]
        return Response(detail)

    def post(self, request):
        serializer = ReactSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

class CheckView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    def post(self, request):
        print(request)
        return Response("str_img")
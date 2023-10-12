from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from rest_framework.response import Response
from .serializer import *
from rest_framework.parsers import MultiPartParser, FormParser
import face_recognition as fr
from .utils import is_ajax, classify_face
import os


# Create your views here.


class AddView(APIView):
    serializer_class = ReactSerializer
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request):
        detail = [
            {
                "name": detail.name,
                "address": detail.address,
                "username": detail.username,
            }
            for detail in React.objects.all()
        ]
        return Response(detail)

    def post(self, request):
        print(request.data)
        serializer = ReactSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


class CheckView(APIView):
    serializer_class = CheckSerializer
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        serializer = CheckSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            print(fr.load_image_file(serializer.data["photo"][1:]))
            res = classify_face(serializer.data["photo"][1:])
            print("heyyy")
            print(res)
            if res:
                print("here")
                user_exists = React.objects.filter(username=res).exists()
                print(user_exists)
                if user_exists:
                    user = React.objects.get(username=res)
                    detail = {
                        "name": user.name,
                        "address": user.address,
                        "username": user.username,
                    }

                    return Response(detail)
                return Response("User does not exist")

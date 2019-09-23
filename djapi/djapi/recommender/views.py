# Django/Django-RestAPI imports
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
# Custom module imports
from djapi.recommender.serializers import (
    UserSerializer, GroupSerializer, UserRatingSerializer, StrainSerializer)
from .models import UserRating, Strain


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


@csrf_exempt
def strain_list(request):
    """
    List all strains or create new strain
    """
    if request.method == 'GET':
        strains = Strain.objects.all()
        serializer = StrainSerializer(strains, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = StrainSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def strain_detail(request, pk):
    """
    Retrieve, update, or delete a strain.
    """
    try:
        strain = Strain.objects.get(pk=pk)
    except Strain.DoesNotExist:
        return HttpResponse(status=400)

    if request.method == 'GET':
        serializer = StrainSerializer(strain)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = StrainSerializer(strain, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        strain.delete()
        return HttpResponse(status=204)


@csrf_exempt
def userrating_list(request):
    """
    List all userratings or create new userrating
    """
    if request.method == 'GET':
        userratings = UserRating.objects.all()
        serializer = UserRatingSerializer(userratings, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserRatingSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def userrating_detail(request, pk):
    """
    Retrieve, update, or delete a userrating.
    """
    try:
        userrating = UserRating.objects.get(pk=pk)
    except userrating.DoesNotExist:
        return HttpResponse(status=400)

    if request.method == 'GET':
        serializer = UserRatingSerializer(userrating)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserRatingSerializer(userrating, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        userrating.delete()
        return HttpResponse(status=204)

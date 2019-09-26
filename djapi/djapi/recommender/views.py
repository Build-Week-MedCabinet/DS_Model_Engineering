# Django/Django-RestAPI imports
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.core.cache import cache
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import (
    BasePermission, IsAuthenticated, SAFE_METHODS)
# Custom module imports
from djapi.recommender.serializers import (
    UserSerializer, GroupSerializer, UserRatingSerializer, StrainSerializer)
from djapi.recommender.models import UserRating, Strain
from djapi.recommender.dataprocessing import process_request
from djapi.recommender.predictor import Predictor
# Debug and Logging
import logging


logger = logging.getLogger(__name__)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]


class StrainViewSet(viewsets.ModelViewSet):
    """
    API endpiont that allows strains to be viewed or edited
    """
    queryset = Strain.objects.all()
    serializer_class = StrainSerializer



class UserRatingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows user ratings to be viewed or edited
    """
    queryset = UserRating.objects.all()
    serializer_class = UserRatingSerializer


@api_view(['GET'])
def recommender_view(request):
    """
    API endpoint that allows querying recommender with features.
    """
    if request.method == 'GET':
        data = process_request(request)
        logger.info(request)
        logger.info(data)
        # check cache for predictor.  if none exists, instantiate new predictor.
        # try:
        #     if not cache.get('predictor'):
        #         predictor = Predictor()
        #     else:
        #         predictor = cache.get('predictor')
        # except:
        #     print('cache unavailable?')
        #     predictor = Predictor()
        # Run predictor
        predictor = Predictor()
        predictor.transform(data)
        recommendation = predictor.get_recommendation()

        return Response(recommendation)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

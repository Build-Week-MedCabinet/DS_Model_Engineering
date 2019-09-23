# Django/Django-RestAPI imports
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
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
    demo_data = [{"Strain":"Ghost-Ship","Type":"indica","Rating":4.0,"Effects":"Relaxed,Happy,Sleepy,Euphoric,Tingly","Flavor":"Earthy,Pungent,Skunk","Description":"Ghost Ship is an indica-dominant cross between Purple Kush Starship and Gupta Kush created by Colorado Seed Inc. Pervasive relaxation cascades over the body, but the buzz is not lethargic. With a very strong aroma that can only be described as \u201cKushy,\u201d this strain soothes aches and pains while lending heady introspection. Think hard and rest easy. This flower is a solid option for muscle relaxation and stress relief. \u00a0"},{"Strain":"Sfv-Og-Kush","Type":"indica","Rating":4.5,"Effects":"Relaxed,Happy,Euphoric,Uplifted,Sleepy","Flavor":"Pine,Earthy,Lemon","Description":"SFV OG Kush, not to be confused with its precursor SFV OG, is an indica-dominant strain bred from OG Kush genetics by The Cali Connection. By crossing an SFV OG clone with an Afghani father and selecting for favorable traits over several generations, the indica-heavy SFV OG Kush was born. You can smell the OG genes in this one, as its odor is commonly described as a strong lemon cleaner smell intermixed with pine."},{"Strain":"Blue-Boy","Type":"hybrid","Rating":4.1,"Effects":"Happy,Relaxed,Giggly,Euphoric,Aroused","Flavor":"Earthy,Pungent,Flowery","Description":"Blue Boy is a cross of popular favorites Blue Dream and Northern Lights #5 that will give you anything but the blues. Originally from Washington state, this sativa-dominant hybrid provides focused, cerebral effects that make it a great choice for daytime use. Its plants are bushy and grow large, and the flowers tend to be large and on the looser, leafier side. Blue Boy is a potent strain with THC levels that often test over 20%."},{"Strain":"Fruity-Pebbles","Type":"hybrid","Rating":4.4,"Effects":"Happy,Relaxed,Uplifted,Euphoric,Giggly","Flavor":"Sweet,Tropical,Berry","Description":"Fruity Pebbles (AKA Fruity Pebbles OG) by Alien Genetics was a limited-time offering from the breeder. This sweet hybrid takes genetics from Green Ribbon, Granddaddy Purple, and Tahoe Alien\u00a0to create a tropical, berry flavor reminiscent of the cereal. The euphoric effects will keep you happy when you\u2019re stressed and help you catch some sleep when faced with insomnia. Sit back, relax, and pour yourself a bowl of Fruity Pebbles!"},{"Strain":"Six-Shooter","Type":"hybrid","Rating":4.6,"Effects":"Creative,Euphoric,Happy,Uplifted,Focused","Flavor":"Sweet,Skunk,Citrus","Description":"Six Shooter by Royal Dutch Genetics is a six-way cross that comes out as a sativa-dominant hybrid with effects as diverse as its lineage. By crossing Haze, Super Skunk, Northern Lights, Brazilian, Royal Dutch, and Trainwreck, this strain achieves a symphony of effects that lean ever so gently toward the stimulating side, complementing the latent indica effect nestled deep between the\u00a0calyxes of this flower. Its effects can inspire appetite, subdue anxiety and mild physical pain, and offer a pleasant euphoria that is quick to arrive and slow to fade"}]
    print(request)
    return Response(demo_data)
    # return JsonResponse(demo_data, safe=False)

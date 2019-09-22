from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import UserRating, Strains


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class UserRatingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserRating
        fields = [
            'created', 'username', 'userclass',
            'strain_name', 'rating'
            ]


class StrainsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Strains
        fields = [
            'created', 'updated',
            'strain_name', 'strain_effect_list', 'strain_flavor_list',
            'strain_desc', 'strain_effect_embed', 'strain_flavor_embed',
            'strain_desc_embed'
            ]
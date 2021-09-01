from django.contrib.auth.models import User, Group
from rest_framework import serializers
from poetry.models import Poet, Era, Poem


class PoetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poet
        fields = ['id', 'name', 'era']


class EraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Era
        fields = ['id', 'name']


class PoemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poem
        fields = ['id', 'head', 'poet']


class OnePoemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poem
        fields = ['id', 'head', 'body', 'poet']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

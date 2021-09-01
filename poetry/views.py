from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import api_view

from poetry.serializers.serializers import UserSerializer, GroupSerializer, EraSerializer, PoemSerializer, \
    OnePoemSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from poetry.models import Poet, Era, Poem
from poetry.serializers.serializers import PoetSerializer
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def poets_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        poets = Poet.objects.all()
        serializer = PoetSerializer(poets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PoetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def eras_list(request):
    eras = Era.objects.all()
    serializer = EraSerializer(eras, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def list_poems_of_this_poet(request, poet_id):
    his_poems = Poem.objects.filter(poet=poet_id)
    serializer = PoemSerializer(his_poems, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def poem(request, poem_id):
    one_poem = Poem.objects.get(pk=poem_id)
    serializer = OnePoemSerializer(one_poem)
    return Response(serializer.data)


@api_view(['GET'])
def know_who(request):
    data = {
        'user' : str(request.user),
        'auth': str(request.auth),
    }
    return Response(data)




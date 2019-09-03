# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from rest_framework import status
from rest_framework import viewsets


# Create your views here.
class HelloApiView(APIView):
    """Rest Api View"""

    serializer_class = serializers.HelloSerializer

    def get(self,request,format=None):
        """return a list of api view features"""

        an_apiview = [
            'Uses HTTP methods as function (get,post,put,patch,delete)',
            'it is similar to a traditional django view',
            'Gives you the most control over your logic',
            'IS mapped manaually to urls'
        ]

        return Response({'message':'Hello!', 'an_api':an_apiview})

    def post(self,request):
        """create a hello messsge with our name"""

        serializer = serializers.HelloSerializer(data = request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)

            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):

        return Response({'method':'put'})

    def patch(self, request,pk=None):

        return Response({'method':'patch'})

    def delete(self, request,pk=None):
        return Response({'method':'delete'})


class HelloViewset(viewsets.ViewSet):
    """Test API Viewsets"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message"""

        a_viewset = [
            'uses actions (list, create, retrive, update, partial_update)',
            'Automatically update the urls using routers',
            'provide more functanality with less code.'
        ]

        return Response({'message':'hello!','viewset':a_viewset})

    def create(self, request):
        """CREATE A NEW HELLO MESSAGE"""
        serializer = serializers.HelloSerializer(data= request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})

        else:
            return Response(serializer.errors, status=satus.HTTP_400_BAD_REQUEST)

    def retrive(self, request):
        """ Handles getting an object by its id """
        return Response({'http_method':'get'})

    def update(self, request, pk=None):
        """ handles updating an object """
        return Response({'http_method':'put'})

    def partial_update(self, request, pk=None):
        """handles partial updates of an object """
        return Response({'http_method':'patch'})

    def destroy(self, request, pk=None):
        """ delete an object """
        return Response({'http_method':'delete'})

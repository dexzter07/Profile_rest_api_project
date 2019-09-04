# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from rest_framework import status
from rest_framework import viewsets
from . import models
from . import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated


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

class UserProfileViewset(viewsets.ModelViewSet):
    """HANDLES CREATING, CREATING AND UPDATING PROFILES"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)


class LoginViewSet(viewsets.ViewSet):
    """checks email and password and return auth token."""

    serializer_class = AuthTokenSerializer

    def create(self, request):
        """use the ObtainAuthToken APIView to validate and create a token"""

        return ObtainAuthToken().post(request)

class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed items"""

    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemsSerializer
    queryset = models.ProfileFeedItems.objects.all()
    permission_classes = (permissions.PostOwnStatus, IsAuthenticated)

    def perform_create(self, serializer):
        """sets the user profile to the logged in users"""

        serializer.save(user_profile=self.request.user)

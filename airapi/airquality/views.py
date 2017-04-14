# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from airquality.models import Rule, Record, Alert, Person
from airquality.serializers import RuleSerializer, UserSerializer, RecordSerializer, AlertSerializer, PersonSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework import viewsets, mixins
from rest_framework.decorators import detail_route

class PersonViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RuleViewSet(viewsets.ModelViewSet):

    queryset = Rule.objects.all()
    serializer_class = RuleSerializer

class RecordViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):

    queryset = Record.objects.all()
    serializer_class = RecordSerializer

class AlertViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer

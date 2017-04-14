# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Rule(models.Model):
    parameter = models.CharField(max_length=30)
    threshold = models.IntegerField(default=0)
    owners = models.ManyToManyField(User)

    class Meta:
        ordering = ('parameter',)

class Alert(models.Model):
    received =  models.DateTimeField(auto_now_add=True)
    parameter =  models.CharField(max_length=30)
    value = models.IntegerField(default=0);
    threshold = models.IntegerField(default=0)
    owners =  models.ManyToManyField(User)

    class Meta:
        ordering = ('received',)

class Record(models.Model):
    received = models.DateTimeField(auto_now_add=True)
    parameter = models.CharField(max_length=30)
    value = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        objs = Rule.objects.filter(parameter=self.parameter, threshold__lte=self.value)
        if len(objs) > 0:
            for obj in objs:
		a = Alert.objects.create(parameter=self.parameter, value=self.value, threshold=obj.threshold)
                a.save()
                a.owners.add(*obj.owners.all())
		
                #a = Alert.objects.create(parameter=self.parameter, value=self.value, threshold=obj.threshold, owners=obj.owners)

        super(Record, self).save(*args, **kwargs)
             

    class Meta:
        ordering = ('received',)

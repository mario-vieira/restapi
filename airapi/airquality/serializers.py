from rest_framework import serializers
from airquality.models import Rule, Record, Alert
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class UsernameSerializer(serializers.HyperlinkedModelSerializer):
    #owner = serializers.CharField(read_only=True, source='owner.username')
    
    class Meta:
        model = User
        fields = ('username',)

class RuleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rule
        fields = ('url', 'parameter','threshold','owners')

class RecordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Record
        fields = ('url', 'received','parameter','value')

class AlertSerializer(serializers.HyperlinkedModelSerializer):
    #owners = serializers.ReadOnlyField(source='owners.username')
    owners = UserSerializer(many=True)
    class Meta:
        model = Alert
        fields = ('url', 'received','parameter','value', 'threshold', 'owners')

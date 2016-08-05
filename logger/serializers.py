from rest_framework import serializers
from django.contrib.auth.models import User
from logger.models import *

class BMSSerializer(serializers.ModelSerializer):
    class Meta:
        model = BMSData
        fields = ('id', 'name','btq1','btq2','btq3','btq4')

class MCSerializer(serializers.ModelSerializer):
    class Meta:
        model = MCData
        fields = ('id', 'name','mct','mc2mlc','mc2mrc','mc2bc','maxdiscC','mindiscC','maxc')

class GeneralSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralData
        fields = ('id', 'name','speedfl','speedfr','speedbl','speedbr','soc')

class MotorSerializer(serializers.ModelSerializer):
	class Meta:
		model = MotorData
		fields = ('id','name','mtr','mtl')


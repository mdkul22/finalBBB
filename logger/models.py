from django.db import models

class BMSData(models.Model):
	name = models.CharField(max_length=10, default='BMS', editable=False)
	btq1 = models.CommaSeparatedIntegerField(max_length=100)
	btq2 = models.CommaSeparatedIntegerField(max_length=100)
	btq3 = models.CommaSeparatedIntegerField(max_length=100)
	btq4 = models.CommaSeparatedIntegerField(max_length=100)

class MCData(models.Model):
	name = models.CharField(max_length=10, default='MOTOR CONTROLLER', editable=False)
	mct = models.CommaSeparatedIntegerField(max_length=100)
	mc2mlc = models.CommaSeparatedIntegerField(max_length=100)
	mc2mrc = models.CommaSeparatedIntegerField(max_length=100)
	mc2bc = models.CommaSeparatedIntegerField(max_length=100)
	maxdiscC = models.CommaSeparatedIntegerField(max_length=100)
	mindiscC = models.CommaSeparatedIntegerField(max_length=100)
	maxc =models.CommaSeparatedIntegerField(max_length=100)

class GeneralData(models.Model):
	name = models.CharField(max_length=10,default='GENERAL', editable=False)
	speedfl = models.CommaSeparatedIntegerField(max_length=100)
	speedfr = models.CommaSeparatedIntegerField(max_length=100)
	speedbl = models.CommaSeparatedIntegerField(max_length=100)
	speedbr = models.CommaSeparatedIntegerField(max_length=100)
	soc = models.CommaSeparatedIntegerField(max_length=100)

class MotorData(models.Model):
	name = models.CharField(max_length=10,default='MOTOR', editable=False)
	mtr = models.CommaSeparatedIntegerField(max_length=100)
	mtl = models.CommaSeparatedIntegerField(max_length=100)


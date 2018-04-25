from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.


class DolotoDiametr(models.Model):
	id = models.AutoField(primary_key=True)
	MinDiametr = models.DecimalField(max_digits=5, decimal_places=2)
	MaxDiametr = models.DecimalField(max_digits=5, decimal_places=2)
	def  __str__(self):
		return str(self.MaxDiametr)

class DiametrYBT(models.Model):
	id = models.AutoField(primary_key=True)
	diametrYBT = models.IntegerField(default=0)
	weightYBT = models.DecimalField(max_digits=5, decimal_places=1, default=0)
	def __str__(self):
		return str(self.diametrYBT)

class DolotoWithYBT(models.Model):
	id = models.AutoField(primary_key=True)
	doloto = models.ForeignKey(DolotoDiametr, on_delete=models.PROTECT)
	ybt = models.ForeignKey(DiametrYBT, on_delete=models.PROTECT)
	def __str__(self):
		return str(self.doloto)

class CasingDiametr(models.Model):
	id = models.AutoField(primary_key=True)
	casingValue = models.DecimalField(max_digits=5, decimal_places=2)
	def __str__(self):
		return str(self.casingValue)

class CasingWithYBT(models.Model):
	id = models.AutoField(primary_key=True)
	ybt = models.ForeignKey(DiametrYBT, on_delete=models.PROTECT)
	casing = models.ForeignKey(CasingDiametr, on_delete=models.PROTECT)
	def __str__(self):
		return str(self.ybt)+'-'+str(self.casing)
		
class BoringDiametr(models.Model):
	id = models.AutoField(primary_key=True)
	boring = models.IntegerField(default=0)
	def __str__(self):
		return str(self.boring)	

class BoringWithCasing(models.Model):
	id = models.AutoField(primary_key=True)
	boring = models.ForeignKey(BoringDiametr, on_delete=models.PROTECT)
	casing = models.ForeignKey(CasingDiametr, on_delete=models.PROTECT)
	def __str__(self):
		return str(self.boring)+'-'+str(self.casing)

class engine(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=200)
	weight = models.IntegerField(default=0)
	def __str__(self):
		return self.name

class historyСalc(models.Model):
	id = models.AutoField(primary_key=True)
	pub_date = models.DateTimeField('date published', default=datetime.datetime.now())
	davl = models.IntegerField(default=0)
	result = models.DecimalField(max_digits=6, decimal_places=2)
	user = models.ForeignKey(User, default=0)
	def __str__(self):
		return str(self.result)
		

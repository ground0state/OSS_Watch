from django.db import models

# Create your models here.

class Info(models.Model):
	
	#OSSのバージョン
	version = models.CharField(max_length=128)
	
	#OSSのリリース日
	released = models.DateField()
	
	#スクレイピングした日
	registrated = models.DateTimeField()
	
	#ossの関係づけ
	oss = models.ForeignKey('Oss',on_delete=models.CASCADE)
	
	class Meta:
		unique_together = (('version', 'oss'))

class Oss(models.Model):
	
	#OSSのid
	oss_id = models.IntegerField(primary_key=True)
	
	#OSSの名前
	oss_name = models.CharField(max_length=128)
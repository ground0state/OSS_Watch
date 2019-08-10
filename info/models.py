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
    
    def __repr__(self):
        # 主キーとnameを表示させて見やすくする
        return "{}: {}".format(self.oss_id, self.oss_name)

    __str__ = __repr__
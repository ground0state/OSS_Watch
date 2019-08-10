from django.db import models

# Create your models here.

class Info(models.Model):
    
    #OSS�̃o�[�W����
    version = models.CharField(max_length=128)
    
    #OSS�̃����[�X��
    released = models.DateField()
    
    #�X�N���C�s���O������
    registrated = models.DateTimeField()
    
    #oss�̊֌W�Â�
    oss = models.ForeignKey('Oss',on_delete=models.CASCADE)
    
    class Meta:
        unique_together = (('version', 'oss'))

class Oss(models.Model):
    
    #OSS��id
    oss_id = models.IntegerField(primary_key=True)
    
    #OSS�̖��O
    oss_name = models.CharField(max_length=128)
    
    def __repr__(self):
        # ��L�[��name��\�������Č��₷������
        return "{}: {}".format(self.oss_id, self.oss_name)

    __str__ = __repr__
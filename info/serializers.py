from rest_framework import serializers
from info.models import Info, Oss




class OssSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oss
        fields = ('oss_id', 'oss_name',)
        #fields = '__all__'


class InfoSerializer(serializers.ModelSerializer):
    oss = OssSerializer()
    class Meta:
        model = Info
        fields = ('version', 'released', 'oss',)
 

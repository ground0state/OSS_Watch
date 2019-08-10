from rest_framework import viewsets, routers, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from info.models import Info,Oss
from info.serializers import InfoSerializer,OssSerializer
import django_filters
 
class InfoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Info.objects.all()
    serializer_class = InfoSerializer
    filter_fields = ('oss_id',)

class OssViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Oss.objects.all()
    serializer_class = OssSerializer

router = routers.DefaultRouter()
router.register(r'info_list', InfoViewSet)
router.register(r'oss_list', OssViewSet)
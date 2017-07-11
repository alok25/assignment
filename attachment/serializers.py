from attachments.models import AssetsManagement
from audetemi.non_null_serializer import BaseSerializer


class AssetsManagementSerializer(BaseSerializer):
    class Meta:
        model = AssetsManagement

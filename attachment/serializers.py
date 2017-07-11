from attachment.models import AssetsManagement
from assignment.non_null_serializer import BaseSerializer


class AssetsManagementSerializer(BaseSerializer):
    class Meta:
        model = AssetsManagement

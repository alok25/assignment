import json
import os

from django.core.files.base import ContentFile
from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from assignment.settings import BASE_DIR
from attachment.models import AssetsManagement
from attachment.serializers import AssetsManagementSerializer


class AssetsManagementCreateViewMultipart(CreateAPIView):
    serializer_class = AssetsManagementSerializer
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser,)

    def post(self, request, format=None):
        """
        This method is used to store user's ticket images.
        """
        user_asset_data = request.data

        filename = user_asset_data['name']

        up_file = request.FILES.get('attachment')

        if up_file:
            destination = open(BASE_DIR + '/' +  up_file.name, 'wb+')
            for chunk in up_file.chunks():
                destination.write(chunk)
            destination.close()
            try:
                image_obj = open(BASE_DIR + '/' + up_file.name).read()
                file_content = ContentFile(image_obj,
                                           BASE_DIR + '/' + user_asset_data['name'])
            except:
                return Response({"msg": "Attachment not uploaded successfully."},
                                status=status.HTTP_412_PRECONDITION_FAILED)

            user_asset_data['created_by'] = int(request.user.id)
            user_asset_data['is_active'] = True
            user_asset_data['attachment'] = file_content
            serializer = AssetsManagementSerializer(data=user_asset_data)

            if serializer.is_valid():
                serializer.save()
                os.remove(BASE_DIR + '/' + up_file.name)
                return Response(serializer.data,
                                status=status.HTTP_201_CREATED)
            os.remove(BASE_DIR + '/' + up_file.name)
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"msg": "Attachment not provided"},
                            status=status.HTTP_412_PRECONDITION_FAILED)


class AttachmentListingView(APIView):
    """
    List All the Attachments
    """
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]
    serializer_class = AssetsManagementSerializer

    def get(self, request, format=None):
        """
        This method is used to store user's ticket images.
        """
        if request.user.role == 'Admin':
            data = AssetsManagement.objects.all()
        else:
            data = AssetsManagement.objects.filter(created_by=request.user.id)
        response_dict = {}
        for record in data:
            if record['created_by'] in response_dict:
                response_dict['created_by']['id'] = [record]
            else:
                response_dict['created_by']['id'] = response_dict['created_by']['id'].append(record)
        return Response(json.dumps(response_dict))

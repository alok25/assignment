from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from attachment import views

urlpatterns = [
    url(r'^attachment/upload/$', views.AssetsManagementCreateViewMultipart.as_view(),
        name='file_upload'),
    url(r'^attachment/display/$', views.AttachmentListingView.as_view(),
        name='file_display'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

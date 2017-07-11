from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from user_auth import views

urlpatterns = [
    url(r'^user/register/$', views.CreateUserView.as_view(),
        name='create_user'),
    url(r'^user/login/$', views.LoginView.as_view(),
        name='login'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

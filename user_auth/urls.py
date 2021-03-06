from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from user_auth import views

urlpatterns = [
    url(r'^login/$', views.LoginPageView.as_view(), name='login_page'),
    url(r'^user/register/$', views.CreateUserView.as_view(),
        name='create_user'),
    url(r'^user/login/$', views.LoginView.as_view(),
        name='user_login'),
    url(r'^portal/login/$', views.login,
        name='login'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

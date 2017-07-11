from django.conf.urls import url
from user_auth import views

urlpatterns = [
    url(r'^login/$', views.LoginPageView.as_view(), name='home'),
]

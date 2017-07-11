from django.conf.urls import url
from example import views

urlpatterns = [
    url(r'^login/$', views.LoginPageView.as_view(), name='home'),
]

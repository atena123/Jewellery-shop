from django.conf.urls import url, include
from .views import home, info

urlpatterns = [
    url(r'^home/', home, name="home"),
    url(r'^info/', info, name="info"),
]
from django.urls import path
from .views import createuser,getuser
urlpatterns=[
    path("register/",createuser,name="create_user"),
    path("get/",getuser,name="getuser"),
]
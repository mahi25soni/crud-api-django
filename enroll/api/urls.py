from django.urls import path , include
from rest_framework.routers import DefaultRouter
from .views import StudentViewset

router = DefaultRouter()
router.register('crud', StudentViewset , basename='user')

urlpatterns = [
    path('' , include(router.urls))
]
from django.urls import path, include
from rest_framework import routers
from company.views import CompanyViewSet
from doc.views import DocViewSet
from user.views import UserProfileViewSet

router = routers.DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'docs', DocViewSet)
router.register(r'users', UserProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

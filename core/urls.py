from django.urls import path, include
from .views import Doctor, RegisterUser, Patient, Mapping
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register('patients', Patient)
router.register('doctors', Doctor)
router.register('mappings', Mapping)

urlpatterns = [
    path('auth/register/', RegisterUser.as_view()),
    path('auth/login/', TokenObtainPairView.as_view()),
    path("auth/refresh/", TokenRefreshView.as_view()),
    path('', include(router.urls))
]
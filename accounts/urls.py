from django.urls import path
from .views import RegisterView, UserOnlyView, AdminOnlyView
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/', UserOnlyView.as_view(), name='user-view'),
    path('admin/', AdminOnlyView.as_view(), name='admin-view'),
]
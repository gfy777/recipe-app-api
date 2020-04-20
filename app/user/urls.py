from django.urls import path, include
from .views import CreateUserView, UserLoginView, ManageUserView, UserViewSet
from rest_framework.routers import DefaultRouter

app_name = 'user'

router = DefaultRouter()
router.register('', UserViewSet, basename='user-viewset')

urlpatterns = [
    path('create/', CreateUserView.as_view(), name='create'),
    path('login/', UserLoginView.as_view(), name='token'),
    path('me/', ManageUserView.as_view(), name='me'),
    path('', include(router.urls))
]

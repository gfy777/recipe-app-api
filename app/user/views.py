from rest_framework import generics, authentication, \
    permissions, viewsets, filters
from .serializers import UserSerializer, AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from core.models import User


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer


class UserLoginView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    serializer_class = AuthTokenSerializer
    template_name = 'core/front_end.html'


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""
    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user


# No test below

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """"""
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    authentication_classes = (authentication.TokenAuthentication,)

    queryset = User.objects.all()

    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('name', 'email', 'id')
    ordering_fields = ('name', 'email')

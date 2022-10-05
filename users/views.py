from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from users.models import User
from users.serializers import UserSerializer


class UserView(ListCreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(RetrieveUpdateDestroyAPIView):

	queryset = User.objects.all()
	serializer_class = UserSerializer

	lookup_url_kwarg = "user_id"
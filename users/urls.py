from django.urls import path

from users.views import UserDetailView, UserView

urlpatterns = [
    path("users/", UserView.as_view()),
    path("users/<uuid:user_id>/", UserDetailView.as_view()),
]

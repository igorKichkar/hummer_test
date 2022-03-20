from django.urls import path
from .views import ProfileList, ProfileDetail, Code

urlpatterns = [
    path("", Code.as_view(), name="profile_list"),
    path("profile_list/", ProfileList.as_view(), name="profile_list"),
    path("profile/<int:pk>", ProfileDetail.as_view(), name="profile"),
]

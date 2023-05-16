from django.urls import path, include 
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("", include('django.contrib.auth.urls')),
    path("register/", views.register, name="register"),
    path("sessionstats/", views.sessionstats, name="sessionstats"),
    path("downloads/", views.downloads, name="downloads"),
    path("usersession/<str:session_id>/", views.usersessionstats, name="usersession"),
    path("userstats/<str:user_name>/", views.userstats, name="userstats"),
    path("userovervieuw/", views.userovervieuw, name="userovervieuw"),
    path("leaderboard/", views.leaderboard, name="leaderboard"),
    #path("updateprofile/", views.update_profile, name="updateprofile"),
    #path("sessionupdate/", views.session_update, name="sessionupdate")
]

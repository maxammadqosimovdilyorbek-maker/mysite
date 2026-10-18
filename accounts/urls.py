
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

path("studio/", views.studio, name="studio"),
path("studio/new/", views.project_create, name="project_create"),
path(
    "studio/project/<int:pk>/",
    views.project_detail,
    name="project_detail",
),
path(
    "studio/project/<int:pk>/delete/",
    views.project_delete,
    name="project_delete",
),

    path("", views.home, name="home"),
    path(
        "register/",
        views.register_view,
        name="register",
    ),
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="accounts/login.html"
        ),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(),
        name="logout",
    ),
    path(
        "dashboard/",
        views.dashboard,
        name="dashboard",
    ),
    path("profile/", views.profile, name="profile"),
]

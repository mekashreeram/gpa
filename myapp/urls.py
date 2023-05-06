from django.urls import path
from . import views

urlpatterns = [
  path("", views.home, name='home'),
  path("dashboard/", views.dashboard, name = 'dashboard'),
  path("profile/", views.profile, name = "profile"),
  path("profile/addTarget/", views.addTarget, name = "addTarget"),
  path("profile/addSem/", views.addSem, name = "addSem"),
  path("gpacalculator/", views.index, name = 'index'),
  path("gpacalculator/delete/", views.delete, name = 'delete'),
  path("register/", views.register, name='register'),
  path("login/", views.login, name='login'),
  path("logout/", views.logout, name='logout')
]
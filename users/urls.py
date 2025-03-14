from django.urls import path
from . import views

urlpatterns = [
    path('',views.Users.as_view()),
    path('<int:pk>/tweet',views.UserDetail.as_view()),

]
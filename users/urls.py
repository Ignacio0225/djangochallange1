from django.urls import path
from . import views

urlpatterns = [
    path('',views.Users.as_view()),
    path('<int:pk>',views.UserDetail.as_view()),
    path('<int:pk>/tweets',views.UserTweet.as_view()),
    path('password',views.ChangePW.as_view()),
    path('log-in',views.LogIn.as_view()),
    path('log-out',views.LogOud.as_view()),
    path('me',views.Me.as_view()),
    # path('password',)

]
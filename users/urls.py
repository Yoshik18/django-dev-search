from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.loginUser, name="login"),
    path('register/', views.registerUser, name="register"),
    path('logout/', views.logoutUser, name="logout"),

    path('account/', views.account, name="account"),
    path('editAccount/', views.editAccount, name="editAccount"),

    path('addSkill/', views.createSkill, name="addSkill"),
    path('updateSkill/<str:pk>/', views.updateSkill, name="updateSkill"),


    path('', views.profiles, name="profiles"),
    path('profile/<str:pk>/', views.userProfile, name="user-profile"),

    path('inbox/', views.inbox, name="inbox"),
    path('inbox/<str:pk>', views.message, name="message"),

    path('send-message/<str:pk>/', views.createMessage, name="createMessage"),
]

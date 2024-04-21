from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name="index"),
    path('signup',views.signup,name="signup"),
    path('signin',views.signin,name="signin"),
    path('signout',views.signout,name="signout"),
    path('authenticating-user',views.auth_user,name="auth_user"),
    path('error',views.error,name="error"),
    
    path('test',views.test,name="test"),
    
    path('delete-account',views.delete_account,name="delete-account"),   
]

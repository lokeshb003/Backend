from django.urls import path
from . import views
from app.views import delete_account

urlpatterns = [
    path('', views.index, name='plumber'),
    path('profile', views.profile, name='plumber-profile'),
    path('edit-profile', views.edit_profile, name='plumber-edit-profile'),
    path('products', views.products, name='plumber-products'),
    path('delete-account', delete_account, name='delete-account'),
]
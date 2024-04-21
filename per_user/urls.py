from django.urls import path
from . import views
from app.views import delete_account

urlpatterns = [
    path('', views.index, name='per_user'),
    path('products', views.products, name='per_user-products'),
    path('profile', views.profile, name='per_user-profile'),
    path('edit-profile', views.edit_profile, name='per_user-edit-profile'),
    path('delete-account', delete_account),
]
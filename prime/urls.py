from django.urls import path
from . import views
from app.views import delete_account

urlpatterns = [
    path('', views.index, name='prime'),
    path('profile', views.profile, name='prime-profile'),
    path('edit-profile', views.edit_profile, name='prime-edit-profile'),
    path('products', views.products, name='prime-products'),
    path('delete-account', delete_account, name='delete-account'),
]
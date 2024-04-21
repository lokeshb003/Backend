from django.urls import path
from . import views
from app.views import delete_account

urlpatterns = [
    path('', views.index, name='user-admin'),
    path('create-product', views.create_product, name='create-product'),
    path('view-products', views.view_products, name='view-products'),
    path('edit-product/<str:pc>/', views.edit_product, name='edit-product'),
    path('delete-product/<str:pc>/', views.delete_product, name='delete-product'),
    
    path('clients', views.clients, name='clients'),
    path('approve-user/<str:email>/', views.approve_user, name='approve-user'),
    path('revoke-user/<str:email>/', views.revoke_user, name='revoke-user'),
    path('remove-user/<str:email>/', views.remove_user, name='remove-user'),
    
    path('profile', views.profile, name='user-admin-profile'),
    path('edit-profile', views.edit_profile, name='user-admin-edit-profile'),
    
    path('delete-account', delete_account, name='delete-account'),
]
from django.urls import path
from . import views


urlpatterns = [
    path('items/', views.item_list, name='item_list'),
    path('items/add/', views.item_add, name='item_add'),
    path('items/<int:item_id>/', views.item_detail, name='item_detail'),
    path('items/<int:item_id>/edit/', views.item_update, name='item_update'),
    path('items/<int:item_id>/delete/', views.item_delete, name='item_delete'),
]

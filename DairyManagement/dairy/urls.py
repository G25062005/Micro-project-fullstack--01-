from django.urls import path
from . import views

app_name = 'dairy'

urlpatterns = [
    path('', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    # Admin URLs
    path('panel/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('panel/products/', views.manage_products, name='manage_products'),
    path('panel/products/edit/<int:pk>/', views.edit_product, name='edit_product'),
    path('panel/products/delete/<int:pk>/', views.delete_product, name='delete_product'),
    path('panel/orders/', views.manage_orders, name='manage_orders'),
    path('panel/orders/update/<int:pk>/', views.update_order_status, name='update_order_status'),

    # Customer URLs
    path('shop/', views.shop, name='shop'),
    path('cart/', views.cart, name='cart'),
    path('cart/add/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('cart/update/<int:pk>/', views.update_cart, name='update_cart'),
    path('cart/remove/<int:pk>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('orders/', views.order_history, name='order_history'),  # ✅ corrected
]

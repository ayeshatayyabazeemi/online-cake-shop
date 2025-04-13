
from django.urls import path
from . import views
from django.urls import path
from .views import update_product, delete_product
from .views import add_product
from .views import get_user_details
urlpatterns = [
    path('', views.home, name='home'),
    path('shop/', views.shop, name='shop'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('admin-login/', views.admin_login, name='admin_login'),  # Add this line
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('signup/', views.signup, name='signup'),
    path('user-dashboard/', views.user_dashboard, name='user_dashboard'),

    path('cupcakes/', views.cupcake_view, name='cupcake_view'), 
    path('brownie/',views.brownie_view,name='brownie_view'),
    path('donut/',views.donut_view,name='donut_view'),
    path('cart/',views.cart_view,name='cart_view'),
    path('ourcake/',views.view_ourcake,name='view_ourcake'),
    path('place_order/', views.place_order, name='place_order'),
    path('view_orders/', views.view_orders, name='view_orders'),
    path('products/',views.product_view,name='product_view'),
    path('update_product/', update_product, name='update_product'),
    path('delete_product/', delete_product, name='delete_product'),
    path("add_product/", add_product, name="add_product"),
    path('get_user_details/', get_user_details, name='get_user_details'),

]

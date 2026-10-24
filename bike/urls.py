"""
URL configuration for bike project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from shop import views
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('bikes/', views.bike_catalog, name='bike_catalog'),
    path('parts/', views.spareparts_catalog, name='parts_catalog'),
    path('equipment/', views.equipment_catalog, name='equipment_catalog'),
    path('accessories/', views.accessories_catalog, name='accessories_catalog'),
    path('bike-trainers/', views.bike_trainers_catalog, name='bike_trainers_catalog'),
    
    path('bike/<int:pk>/', views.bike_detail, name='bike_detail'),
    path('part/<int:pk>/', views.part_detail, name='part_detail'),
    path('equipment-item/<int:pk>/', views.equipment_detail, name='equipment_detail'),
    path('accessory/<int:pk>/', views.accessory_detail, name='accessory_detail'),
    path('bike-trainer/<int:pk>/', views.bike_trainer_detail, name='bike_trainer_detail'),
    
    path('cart/', views.cart_view, name='cart_view'),
    path('cart/add/<str:item_type>/<int:item_id>/', views.add_to_cart_view, name='add_to_cart'),
    path('cart/remove/<str:item_type>/<int:item_id>/', views.remove_from_cart_view, name='remove_from_cart'),
    path('cart/update/<str:item_type>/<int:item_id>/', views.update_cart_quantity_view, name='update_cart_quantity'),
    path('checkout/', views.checkout_view, name='checkout_view'),
    path('checkout/place-order/', views.place_order_view, name='place_order'),
    
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('account/', views.account_view, name='account_view'),
    path('account/profile/', views.account_profile, name='account_profile'),
    path('account/orders/', views.account_orders, name='account_orders'),
    path('account/password/', views.account_password, name='account_password'),
    path('account/wishlist/', views.account_wishlist, name='account_wishlist'),
    path('wishlist/toggle/<str:item_type>/<int:item_id>/', views.toggle_wishlist_view, name='toggle_wishlist'),
    
    path('trade-in/', views.trade_in, name='trade_in'),
    path('trade-in/bike/', views.trade_in_bike, name='trade_in_bike'),
    path('trade-in/parts/', views.trade_in_parts, name='trade_in_parts'),
    path('trade-in/equipment/', views.trade_in_equipment, name='trade_in_equipment'),
    path('trade-in/accessories/', views.trade_in_accessories, name='trade_in_accessories'),
    path('trade-in/bike-trainers/', views.trade_in_bike_trainers, name='trade_in_bike_trainers'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
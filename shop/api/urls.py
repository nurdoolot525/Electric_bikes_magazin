from django.urls import path

from .views import (
    AccessoryDetailAPIView,
    AccessoryListCreateAPIView,
    BikeDetailAPIView,
    BikeListCreateAPIView,
    BikeTrainerDetailAPIView,
    BikeTrainerListCreateAPIView,
    BrandDetailAPIView,
    BrandListCreateAPIView,
    CategoryDetailAPIView,
    CategoryListCreateAPIView,
    ColorDetailAPIView,
    ColorListCreateAPIView,
    CountryDetailAPIView,
    CountryListCreateAPIView,
    EquipmentDetailAPIView,
    EquipmentListCreateAPIView,
    FrameMaterialDetailAPIView,
    FrameMaterialListCreateAPIView,
    OrderDetailAPIView,
    OrderItemDetailAPIView,
    OrderItemListCreateAPIView,
    OrderListCreateAPIView,
    ProfileDetailAPIView,
    ProfileListCreateAPIView,
    SparePartDetailAPIView,
    SparePartListCreateAPIView,
    WishlistDetailAPIView,
    WishlistListCreateAPIView,
)

urlpatterns = [
    path('categories/', CategoryListCreateAPIView.as_view(), name='api_categories'),
    path('categories/<int:pk>/', CategoryDetailAPIView.as_view(), name='api_category_detail'),

    path('countries/', CountryListCreateAPIView.as_view(), name='api_countries'),
    path('countries/<int:pk>/', CountryDetailAPIView.as_view(), name='api_country_detail'),

    path('brands/', BrandListCreateAPIView.as_view(), name='api_brands'),
    path('brands/<int:pk>/', BrandDetailAPIView.as_view(), name='api_brand_detail'),

    path('frame-materials/', FrameMaterialListCreateAPIView.as_view(), name='api_frame_materials'),
    path('frame-materials/<int:pk>/', FrameMaterialDetailAPIView.as_view(), name='api_frame_material_detail'),

    path('colors/', ColorListCreateAPIView.as_view(), name='api_colors'),
    path('colors/<int:pk>/', ColorDetailAPIView.as_view(), name='api_color_detail'),

    path('bikes/', BikeListCreateAPIView.as_view(), name='api_bikes'),
    path('bikes/<int:pk>/', BikeDetailAPIView.as_view(), name='api_bike_detail'),

    path('parts/', SparePartListCreateAPIView.as_view(), name='api_parts'),
    path('parts/<int:pk>/', SparePartDetailAPIView.as_view(), name='api_part_detail'),

    path('equipment/', EquipmentListCreateAPIView.as_view(), name='api_equipment'),
    path('equipment/<int:pk>/', EquipmentDetailAPIView.as_view(), name='api_equipment_detail'),

    path('accessories/', AccessoryListCreateAPIView.as_view(), name='api_accessories'),
    path('accessories/<int:pk>/', AccessoryDetailAPIView.as_view(), name='api_accessory_detail'),

    path('trainers/', BikeTrainerListCreateAPIView.as_view(), name='api_trainers'),
    path('trainers/<int:pk>/', BikeTrainerDetailAPIView.as_view(), name='api_trainer_detail'),

    path('orders/', OrderListCreateAPIView.as_view(), name='api_orders'),
    path('orders/<int:pk>/', OrderDetailAPIView.as_view(), name='api_order_detail'),

    path('order-items/', OrderItemListCreateAPIView.as_view(), name='api_order_items'),
    path('order-items/<int:pk>/', OrderItemDetailAPIView.as_view(), name='api_order_item_detail'),

    path('profiles/', ProfileListCreateAPIView.as_view(), name='api_profiles'),
    path('profiles/<int:pk>/', ProfileDetailAPIView.as_view(), name='api_profile_detail'),

    path('wishlist/', WishlistListCreateAPIView.as_view(), name='api_wishlist'),
    path('wishlist/<int:pk>/', WishlistDetailAPIView.as_view(), name='api_wishlist_detail'),
]

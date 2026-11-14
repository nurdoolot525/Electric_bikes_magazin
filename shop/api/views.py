from rest_framework import generics, status
from rest_framework.response import Response

from shop.models import Bike, SparePart, Equipment, Accessory, BikeTrainer, Category, Country, Brand, FrameMaterial, Color, Order, OrderItem, Profile, Wishlist
from .serializers import (
    BikeSerializer,
    SparePartSerializer,
    EquipmentSerializer,
    AccessorySerializer,
    BikeTrainerSerializer,
    CategorySerializer,
    CountrySerializer,
    BrandSerializer,
    FrameMaterialSerializer,
    ColorSerializer,
    OrderSerializer,
    OrderItemSerializer,
    ProfileSerializer,
    WishlistSerializer,
)


class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CountryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CountryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class BrandListCreateAPIView(generics.ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class BrandDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class FrameMaterialListCreateAPIView(generics.ListCreateAPIView):
    queryset = FrameMaterial.objects.all()
    serializer_class = FrameMaterialSerializer


class FrameMaterialDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FrameMaterial.objects.all()
    serializer_class = FrameMaterialSerializer


class ColorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer


class ColorDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer


class BikeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Bike.objects.all()
    serializer_class = BikeSerializer


class BikeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bike.objects.all()
    serializer_class = BikeSerializer


class SparePartListCreateAPIView(generics.ListCreateAPIView):
    queryset = SparePart.objects.all()
    serializer_class = SparePartSerializer


class SparePartDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SparePart.objects.all()
    serializer_class = SparePartSerializer


class EquipmentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer


class EquipmentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer


class AccessoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Accessory.objects.all()
    serializer_class = AccessorySerializer


class AccessoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Accessory.objects.all()
    serializer_class = AccessorySerializer


class BikeTrainerListCreateAPIView(generics.ListCreateAPIView):
    queryset = BikeTrainer.objects.all()
    serializer_class = BikeTrainerSerializer


class BikeTrainerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BikeTrainer.objects.all()
    serializer_class = BikeTrainerSerializer


class OrderListCreateAPIView(generics.ListCreateAPIView):
    queryset = Order.objects.all().order_by('-created_at')
    serializer_class = OrderSerializer


class OrderDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderItemListCreateAPIView(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class OrderItemDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class ProfileListCreateAPIView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class WishlistListCreateAPIView(generics.ListCreateAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer


class WishlistDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer

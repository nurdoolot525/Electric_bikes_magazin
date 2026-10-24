from django.contrib import admin

from .models import Category, Bike, Country, BikeImages, SparePart, Accessory, Equipment, Brand, FrameMaterial, Color, BikeTrainer, Order, OrderItem


class BikeImagesAdmin(admin.TabularInline):
    model = BikeImages
    extra = 1

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Bike)
class BikeAdmin(admin.ModelAdmin):
    list_display = ['name','price','image','color','in_stock']
    list_editable = ['in_stock']
    list_filter = ['category','in_stock','color','price','brand','frame_material']
    search_fields = ['brand','color']
    inlines = [BikeImagesAdmin]

@admin.register(SparePart)
class SparePartAdmin(admin.ModelAdmin):
    list_display = ['name','price','image','category','in_stock']
    list_editable = ['in_stock']
    list_filter = ['category','in_stock','price']
    search_fields = ['name','category']

@admin.register(Accessory)
class AccessoryAdmin(admin.ModelAdmin):
    list_display = ['name','price','image','category','in_stock']
    list_editable = ['in_stock']
    list_filter = ['category','in_stock','price']
    search_fields = ['name','category']
    
@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'brand', 'price', 'color', 'in_stock']
    list_editable = ['in_stock']
    list_filter = ['in_stock', 'brand', 'color']
    
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name']
    
@admin.register(FrameMaterial)
class FrameMaterialAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ['name', 'hex_code'] 
    
@admin.register(BikeTrainer)
class BikeTrainerAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'in_stock']
    list_editable = ['in_stock']
    

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'phone', 'total', 'created_at']
    inlines = [OrderItemInline]
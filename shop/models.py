from django.db import models
import os
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Country(models.Model):
    name = models.CharField(max_length=150, verbose_name='Страна')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'
        
        
class Brand(models.Model):
    name = models.CharField(max_length=150, verbose_name='Бренд')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'



class BaseProduct(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    image = models.ImageField(upload_to='products/')
    description = models.TextField(blank=True)
    in_stock = models.BooleanField(default=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    class Meta:
        abstract = True
        

class FrameMaterial(models.Model):
    name = models.CharField(max_length=100, verbose_name='Материал рамы')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Материал рамы'
        verbose_name_plural = 'Материалы рамы'
        
        
class Color(models.Model):
    name = models.CharField(max_length=50, verbose_name='Цвет')
    hex_code = models.CharField(max_length=7, verbose_name='HEX код', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'


class Bike(BaseProduct):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE, verbose_name='Цвет', blank=True, null=True)
    size = models.CharField(max_length=50,null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name='Бренд')
    year = models.DateField(verbose_name='Год выпуска',blank=True,null=True)
    wheel_diameter = models.DecimalField(max_digits=5, decimal_places=2,blank=True,null=True, verbose_name='Диаметр колеса')
    frame_material = models.ForeignKey(FrameMaterial, on_delete=models.CASCADE, verbose_name='Материал рамы', blank=True, null=True)
    tires = models.CharField(max_length=100,verbose_name='Покрышки',blank=True,null=True)
    fork = models.CharField(max_length=100,verbose_name='Вилка',blank=True,null=True)
    brakes_type = models.CharField(max_length=100,verbose_name='Тип тормозов',blank=True,null=True)
    brake_system = models.CharField(max_length=100,verbose_name='Тормозная система',blank=True,null=True) 
    speeds = models.PositiveIntegerField(verbose_name='Количество скоростей',blank=True,null=True)
    warranty = models.CharField(max_length=100,verbose_name='Гарантия',blank=True,null=True)

    def delete(self, *args, **kwargs):
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        super().delete(*args, **kwargs)


    def __str__(self):
        return f"{self.brand} - {self.category}"
    
    class Meta:
        verbose_name = 'Велосипед'
        verbose_name_plural = 'Велосипеды'


class Equipment(BaseProduct):
    size = models.CharField(max_length=50, verbose_name='Размер', blank=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name='Бренд', blank=True, null=True)
    color = models.ForeignKey(Color, on_delete=models.CASCADE, verbose_name='Цвет', blank=True, null=True)
    category = models.CharField(max_length=100, verbose_name='Категория', blank=True, null=True)

    def delete(self, *args, **kwargs):
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Экипировка'
        verbose_name_plural = 'Экипировка'

        
class SparePart(BaseProduct):
    category = models.CharField(max_length=100, verbose_name='Категория', blank=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name='Бренд', blank=True, null=True)
    color = models.ForeignKey(Color, on_delete=models.CASCADE, verbose_name='Цвет', blank=True, null=True)

    def delete(self, *args, **kwargs):
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Запчасть'
        verbose_name_plural = 'Запчасти'


class Accessory(BaseProduct):
    category = models.CharField(max_length=100,verbose_name='Категория')

    def delete(self, *args, **kwargs):
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Аксессуар'
        verbose_name_plural = 'Аксессуары'


class BikeImages(models.Model):
    image = models.ImageField(verbose_name='Картинка',upload_to='bikes/images/')
    bike = models.ForeignKey(Bike,on_delete=models.CASCADE,related_name='images')

    def delete(self, *args, **kwargs):
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        super().delete(*args, **kwargs)

class BikeTrainer(BaseProduct):
    category = models.CharField(max_length=100, verbose_name='Категория', blank=True, null=True)

    def delete(self, *args, **kwargs):
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Велостанок'
        verbose_name_plural = 'Велостанки'
        
        
class Order(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    city = models.CharField(max_length=100, verbose_name='Город')
    street = models.CharField(max_length=200, verbose_name='Улица')
    house = models.CharField(max_length=20, verbose_name='Дом')
    apartment = models.CharField(max_length=20, blank=True, null=True, verbose_name='Квартира')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    email = models.EmailField(verbose_name='E-mail')
    comment = models.TextField(blank=True, null=True, verbose_name='Комментарий')
    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Итого')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата заказа')

    def __str__(self):
        return f"Заказ №{self.id} от {self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    item_type = models.CharField(max_length=20, verbose_name='Тип товара')
    item_id = models.PositiveIntegerField(verbose_name='ID товара')
    item_name = models.CharField(max_length=255, verbose_name='Название товара')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    quantity = models.PositiveIntegerField(verbose_name='Количество')

    def __str__(self):
        return f"{self.item_name} x{self.quantity}"

    class Meta:
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказе'
        


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    display_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Отображаемое имя')
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name='Телефон')
    city = models.CharField(max_length=100, blank=True, null=True, verbose_name='Город')
    street = models.CharField(max_length=200, blank=True, null=True, verbose_name='Улица')
    house = models.CharField(max_length=20, blank=True, null=True, verbose_name='Дом')
    floor = models.CharField(max_length=20, blank=True, null=True, verbose_name='Этаж')
    apartment = models.CharField(max_length=20, blank=True, null=True, verbose_name='Квартира')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):

    if hasattr(instance, 'profile'):
        instance.profile.save()
        
class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wishlist_items')
    item_type = models.CharField(max_length=20, verbose_name='Тип товара')
    item_id = models.PositiveIntegerField(verbose_name='ID товара')
    added_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    class Meta:
        verbose_name = 'Список желаний'
        verbose_name_plural = 'Списки желаний'
        unique_together = ('user', 'item_type', 'item_id')
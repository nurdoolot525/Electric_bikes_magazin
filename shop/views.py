from django.shortcuts import render, redirect
from .models import Bike, Category, Country, Brand, FrameMaterial, Color,SparePart, Equipment, Accessory, BikeTrainer, Order, OrderItem, Profile, Wishlist
from django.core.paginator import Paginator

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required




def bike_catalog(request):
    bikes = Bike.objects.all()
    categories = Category.objects.all()
    brands = Brand.objects.all()
    frame_materials = FrameMaterial.objects.all()
    colors = Color.objects.all()
    

    in_stock = request.GET.get('in_stock')
    if in_stock:
        bikes = bikes.filter(in_stock=True)

    category = request.GET.get('category')
    if category:
        bikes = bikes.filter(category_id=category)


    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    if min_price:
        bikes = bikes.filter(price__gte=min_price)

    if max_price:
        bikes = bikes.filter(price__lte=max_price)
        
    brand = request.GET.get('brand')
    if brand:
        bikes = bikes.filter(brand_id=brand)
        
    frame_material = request.GET.get('frame_material')
    if frame_material:
        bikes = bikes.filter(frame_material_id=frame_material)
        
    color = request.GET.get('color')
    if color:
        bikes = bikes.filter(color_id=color)
        
    sort = request.GET.get('sort')
    if sort == 'old':
        bikes = bikes.order_by('id')
    else:
        bikes = bikes.order_by('-id')
        
        
    paginator = Paginator(bikes, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    page_range = paginator.get_elided_page_range(page_obj.number, on_each_side=1, on_ends=1)
            
        
    context = {
        'bikes': page_obj,
        'page_obj': page_obj,
        'page_range': page_range,
        'categories': categories,
        'brands': brands,
        'frame_materials': frame_materials,
        'colors': colors,
    }
    

    return render(request, 'bike.html', context)


def trade_in(request):
    return render(request, 'trade_in.html')


def trade_in_bike(request):
    categories = Category.objects.all()
    countries = Country.objects.all()
    brands = Brand.objects.all()
    colors = Color.objects.all()
    frame_materials = FrameMaterial.objects.all()

    if request.method == 'POST':
        Bike.objects.create(
            name=request.POST.get('name'),
            category_id=request.POST.get('category'),
            country_id=request.POST.get('country'),
            brand_id=request.POST.get('brand'),
            price=request.POST.get('price'),
            color_id=request.POST.get('color') or None,
            size=request.POST.get('size'),
            year=request.POST.get('year') or None,
            wheel_diameter=request.POST.get('wheel_diameter') or None,
            frame_material_id=request.POST.get('frame_material') or None,
            tires=request.POST.get('tires'),
            fork=request.POST.get('fork'),
            brakes_type=request.POST.get('brakes_type'),
            brake_system=request.POST.get('brake_system'),
            speeds=request.POST.get('speeds') or None,
            warranty=request.POST.get('warranty'),
            description=request.POST.get('description'),
            image=request.FILES.get('image'),
        )
        return redirect('home')

    return render(request, 'trade_in_bike.html', {
        'categories': categories,
        'countries': countries,
        'brands': brands,
        'colors': colors,
        'frame_materials': frame_materials,
    })


def trade_in_parts(request):
    countries = Country.objects.all()
    brands = Brand.objects.all()
    colors = Color.objects.all()

    if request.method == 'POST':
        SparePart.objects.create(
            name=request.POST.get('name'),
            price=request.POST.get('price'),
            country_id=request.POST.get('country'),
            brand_id=request.POST.get('brand'),
            color_id=request.POST.get('color'),
            description=request.POST.get('description'),
            image=request.FILES.get('image'),
        )
        return redirect('home')

    return render(request, 'trade_in_simple.html', {
        'countries': countries,
        'brands': brands,
        'colors': colors,
        'title': 'Продать запчасть',
        'action_url': 'trade_in_parts',
    })


def trade_in_equipment(request):
    countries = Country.objects.all()
    brands = Brand.objects.all()
    colors = Color.objects.all()

    if request.method == 'POST':
        Equipment.objects.create(
            name=request.POST.get('name'),
            price=request.POST.get('price'),
            country_id=request.POST.get('country'),
            brand_id=request.POST.get('brand'),
            color_id=request.POST.get('color'),
            description=request.POST.get('description'),
            image=request.FILES.get('image'),
        )
        return redirect('home')

    return render(request, 'trade_in_simple.html', {
        'countries': countries,
        'brands': brands,
        'colors': colors,
        'title': 'Продать экипировку',
        'action_url': 'trade_in_equipment',
    })
    countries = Country.objects.all()

    if request.method == 'POST':
        Equipment.objects.create(
            name=request.POST.get('name'),
            price=request.POST.get('price'),
            country_id=request.POST.get('country'),
            description=request.POST.get('description'),
            image=request.FILES.get('image'),
        )
        return redirect('home')

    return render(request, 'trade_in_simple.html', {
        'countries': countries,
        'title': 'Продать экипировку',
        'action_url': 'trade_in_equipment',
    })
    countries = Country.objects.all()
    brands = Brand.objects.all()
    colors = Color.objects.all()

    if request.method == 'POST':
        Equipment.objects.create(
            name=request.POST.get('name'),
            price=request.POST.get('price'),
            country_id=request.POST.get('country'),
            description=request.POST.get('description'),
            image=request.FILES.get('image'),
            size='',
            brand='',
            color='',
        )
        return redirect('home')

    return render(request, 'trade_in_simple.html', {
        'countries': countries,
        'title': 'Продать экипировку',
        'action_url': 'trade_in_equipment',
    })


def trade_in_accessories(request):
    countries = Country.objects.all()

    if request.method == 'POST':
        Accessory.objects.create(
            name=request.POST.get('name'),
            price=request.POST.get('price'),
            country_id=request.POST.get('country'),
            description=request.POST.get('description'),
            image=request.FILES.get('image'),
            category='',
        )
        return redirect('home')

    return render(request, 'trade_in_simple.html', {
        'countries': countries,
        'title': 'Продать аксессуар',
        'action_url': 'trade_in_accessories',
    })


def trade_in_bike_trainers(request):
    countries = Country.objects.all()

    if request.method == 'POST':
        BikeTrainer.objects.create(
            name=request.POST.get('name'),
            price=request.POST.get('price'),
            country_id=request.POST.get('country'),
            description=request.POST.get('description'),
            image=request.FILES.get('image'),
        )
        return redirect('home')

    return render(request, 'trade_in_simple.html', {
        'countries': countries,
        'title': 'Продать велостанок',
        'action_url': 'trade_in_bike_trainers',
    })
    categories = Category.objects.all()
    countries = Country.objects.all()
    brands = Brand.objects.all()

    if request.method == 'POST':
        Bike.objects.create(
            name=request.POST.get('name'),
            category_id=request.POST.get('category'),
            country_id=request.POST.get('country'),
            brand_id=request.POST.get('brand'),
            price=request.POST.get('price'),
            color=request.POST.get('color'),
            size=request.POST.get('size'),
            year=request.POST.get('year'),
            wheel_diameter=request.POST.get('wheel_diameter') or None,
            frame_material=request.POST.get('frame_material'),
            tires=request.POST.get('tires'),
            fork=request.POST.get('fork'),
            brakes_type=request.POST.get('brakes_type'),
            brake_system=request.POST.get('brake_system'),
            speeds=request.POST.get('speeds') or None,
            warranty=request.POST.get('warranty'),
            description=request.POST.get('description'),
            image=request.FILES.get('image'),
        )
        return redirect('home')

    return render(request, 'trade_in.html', {'categories': categories, 'countries': countries, 'brands': brands})


def home(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'home.html', context)


def spareparts_catalog(request):
    parts = SparePart.objects.all()
    brands = Brand.objects.all()
    colors = Color.objects.all()

    in_stock = request.GET.get('in_stock')
    if in_stock:
        parts = parts.filter(in_stock=True)

    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    if min_price:
        parts = parts.filter(price__gte=min_price)
    if max_price:
        parts = parts.filter(price__lte=max_price)

    brand = request.GET.get('brand')
    if brand:
        parts = parts.filter(brand_id=brand)

    color = request.GET.get('color')
    if color:
        parts = parts.filter(color_id=color)

    sort = request.GET.get('sort')
    if sort == 'old':
        parts = parts.order_by('id')
    else:
        parts = parts.order_by('-id')

    paginator = Paginator(parts, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    page_range = paginator.get_elided_page_range(page_obj.number, on_each_side=1, on_ends=1)

    context = {
        'parts': page_obj,
        'page_obj': page_obj,
        'page_range': page_range,
        'brands': brands,
        'colors': colors,
        'categories': Category.objects.all(),
    }
    return render(request, 'parts.html', context)


def equipment_catalog(request):
    items = Equipment.objects.all()
    brands = Brand.objects.all()
    colors = Color.objects.all()

    in_stock = request.GET.get('in_stock')
    if in_stock:
        items = items.filter(in_stock=True)

    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    if min_price:
        items = items.filter(price__gte=min_price)
    if max_price:
        items = items.filter(price__lte=max_price)

    brand = request.GET.get('brand')
    if brand:
        items = items.filter(brand_id=brand)

    color = request.GET.get('color')
    if color:
        items = items.filter(color_id=color)

    sort = request.GET.get('sort')
    if sort == 'old':
        items = items.order_by('id')
    else:
        items = items.order_by('-id')

    paginator = Paginator(items, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    page_range = paginator.get_elided_page_range(page_obj.number, on_each_side=1, on_ends=1)

    context = {
        'items': page_obj,
        'page_obj': page_obj,
        'page_range': page_range,
        'brands': brands,
        'colors': colors,
        'categories': Category.objects.all(),
    }
    return render(request, 'equipment.html', context)

def accessories_catalog(request):
    items = Accessory.objects.all()

    in_stock = request.GET.get('in_stock')
    if in_stock:
        items = items.filter(in_stock=True)

    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    if min_price:
        items = items.filter(price__gte=min_price)
    if max_price:
        items = items.filter(price__lte=max_price)

    sort = request.GET.get('sort')
    if sort == 'old':
        items = items.order_by('id')
    else:
        items = items.order_by('-id')

    paginator = Paginator(items, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    page_range = paginator.get_elided_page_range(page_obj.number, on_each_side=1, on_ends=1)

    context = {
        'items': page_obj,
        'page_obj': page_obj,
        'page_range': page_range,
        'categories': Category.objects.all(),
    }
    return render(request, 'accessories.html', context)


def bike_trainers_catalog(request):
    items = BikeTrainer.objects.all()

    in_stock = request.GET.get('in_stock')
    if in_stock:
        items = items.filter(in_stock=True)

    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    if min_price:
        items = items.filter(price__gte=min_price)
    if max_price:
        items = items.filter(price__lte=max_price)

    sort = request.GET.get('sort')
    if sort == 'old':
        items = items.order_by('id')
    else:
        items = items.order_by('-id')

    paginator = Paginator(items, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    page_range = paginator.get_elided_page_range(page_obj.number, on_each_side=1, on_ends=1)

    context = {
        'items': page_obj,
        'page_obj': page_obj,
        'page_range': page_range,
        'categories': Category.objects.all(),
    }
    return render(request, 'bike_trainers.html', context)

def bike_detail(request, pk):
    bike = Bike.objects.get(pk=pk)
    sizes = ['S', 'M-L', 'M', 'L', 'XL']

    similar_bikes = Bike.objects.filter(category=bike.category).exclude(pk=bike.pk)[:8]

    wishlist_ids = []
    if request.user.is_authenticated:
        wishlist_ids = list(
            Wishlist.objects.filter(user=request.user, item_type='bike').values_list('item_id', flat=True)
        )

    return render(request, 'bike_detail.html', {
        'bike': bike,
        'sizes': sizes,
        'similar_bikes': similar_bikes,
        'wishlist_ids': wishlist_ids,
    })
    
def part_detail(request, pk):
    part = SparePart.objects.get(pk=pk)
    similar_items = SparePart.objects.filter(category=part.category).exclude(pk=part.pk)[:8]

    wishlist_ids = []
    if request.user.is_authenticated:
        wishlist_ids = list(
            Wishlist.objects.filter(user=request.user, item_type='part').values_list('item_id', flat=True)
        )

    return render(request, 'part_detail.html', {
        'item': part,
        'similar_items': similar_items,
        'wishlist_ids': wishlist_ids,
    })


def equipment_detail(request, pk):
    item = Equipment.objects.get(pk=pk)
    similar_items = Equipment.objects.filter(category=item.category).exclude(pk=item.pk)[:8]

    wishlist_ids = []
    if request.user.is_authenticated:
        wishlist_ids = list(
            Wishlist.objects.filter(user=request.user, item_type='equipment').values_list('item_id', flat=True)
        )

    return render(request, 'equipment_detail.html', {
        'item': item,
        'similar_items': similar_items,
        'wishlist_ids': wishlist_ids,
    })


def accessory_detail(request, pk):
    item = Accessory.objects.get(pk=pk)
    similar_items = Accessory.objects.filter(category=item.category).exclude(pk=item.pk)[:8]

    wishlist_ids = []
    if request.user.is_authenticated:
        wishlist_ids = list(
            Wishlist.objects.filter(user=request.user, item_type='accessory').values_list('item_id', flat=True)
        )

    return render(request, 'accessory_detail.html', {
        'item': item,
        'similar_items': similar_items,
        'wishlist_ids': wishlist_ids,
    })


def bike_trainer_detail(request, pk):
    item = BikeTrainer.objects.get(pk=pk)
    similar_items = BikeTrainer.objects.filter(category=item.category).exclude(pk=item.pk)[:8]

    wishlist_ids = []
    if request.user.is_authenticated:
        wishlist_ids = list(
            Wishlist.objects.filter(user=request.user, item_type='trainer').values_list('item_id', flat=True)
        )

    return render(request, 'bike_trainer_detail.html', {
        'item': item,
        'similar_items': similar_items,
        'wishlist_ids': wishlist_ids,
    })





# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def cart_view(request):
    cart = request.session.get('cart', {})
    items = []
    total = 0

    for key, qty in cart.items():
        item_type, item_id = key.split('_', 1)

        if item_type == 'bike':
            obj = Bike.objects.get(pk=item_id)
            detail_url = 'bike_detail'
        elif item_type == 'part':
            obj = SparePart.objects.get(pk=item_id)
            detail_url = 'part_detail'
        elif item_type == 'equipment':
            obj = Equipment.objects.get(pk=item_id)
            detail_url = 'equipment_detail'
        elif item_type  == 'accessory':
            obj = Accessory.objects.get(pk=item_id)
            detail_url = 'accessory_detail'
        elif item_type == 'trainer':
            obj = BikeTrainer.objects.get(pk=item_id)
            detail_url = 'bike_trainer_detail'
        else:
            continue

        subtotal = obj.price * qty
        total += subtotal

        items.append({
            'type': item_type,
            'detail_url': detail_url,
            'obj': obj,
            'qty': qty,
            'subtotal': subtotal,
        })

    return render(request, 'cart.html', {
        'items': items,
        'total': total,
    })


def add_to_cart_view(request, item_type, item_id):
    cart = request.session.get('cart', {})
    key = f"{item_type}_{item_id}"

    if key in cart:
        cart[key] = cart[key] + 1
    else:
        cart[key] = 1

    request.session['cart'] = cart
    request.session.modified = True
    return redirect('cart_view')


def remove_from_cart_view(request, item_type, item_id):
    cart = request.session.get('cart', {})
    key = f"{item_type}_{item_id}"

    if key in cart:
        del cart[key]

    request.session['cart'] = cart
    request.session.modified = True
    return redirect('cart_view')


def update_cart_quantity_view(request, item_type, item_id):
    quantity = int(request.POST.get('quantity', 1))
    cart = request.session.get('cart', {})
    key = f"{item_type}_{item_id}"

    if quantity <= 0:
        if key in cart:
            del cart[key]
    else:
        cart[key] = quantity

    request.session['cart'] = cart
    request.session.modified = True
    return redirect('cart_view')



def checkout_view(request):
    cart = request.session.get('cart', {})
    items = []
    total = 0

    for key, qty in cart.items():
        item_type, item_id = key.split('_', 1)

        if item_type == 'bike':
            obj = Bike.objects.get(pk=item_id)
        elif item_type == 'part':
            obj = SparePart.objects.get(pk=item_id)
        elif item_type == 'equipment':
            obj = Equipment.objects.get(pk=item_id)
        elif item_type == 'accessory':
            obj = Accessory.objects.get(pk=item_id)
        elif item_type == 'trainer':
            obj = BikeTrainer.objects.get(pk=item_id)
        else:
            continue

        subtotal = obj.price * qty
        total += subtotal

        items.append({
            'type': item_type,
            'id': item_id,
            'obj': obj,
            'qty': qty,
            'subtotal': subtotal,
        })

    return render(request, 'checkout.html', {
        'items': items,
        'total': total,
    })


def place_order_view(request):
    if request.method == 'POST':
        cart = request.session.get('cart', {})
        items = []
        total = 0

        for key, qty in cart.items():
            item_type, item_id = key.split('_', 1)

            if item_type == 'bike':
                obj = Bike.objects.get(pk=item_id)
            elif item_type == 'part':
                obj = SparePart.objects.get(pk=item_id)
            elif item_type == 'equipment':
                obj = Equipment.objects.get(pk=item_id)
            elif item_type == 'accessory':
                obj = Accessory.objects.get(pk=item_id)
            elif item_type == 'trainer':
                obj = BikeTrainer.objects.get(pk=item_id)
            else:
                continue

            subtotal = obj.price * qty
            total += subtotal

            items.append({
                'type': item_type,
                'id': item_id,
                'name': obj.name,
                'price': obj.price,
                'qty': qty,
            })

        order = Order.objects.create(
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            city=request.POST.get('city'),
            street=request.POST.get('street'),
            house=request.POST.get('house'),
            apartment=request.POST.get('apartment'),
            phone=request.POST.get('phone'),
            email=request.POST.get('email'),
            comment=request.POST.get('comment'),
            total=total,
        )

        for entry in items:
            OrderItem.objects.create(
                order=order,
                item_type=entry['type'],
                item_id=entry['id'],
                item_name=entry['name'],
                price=entry['price'],
                quantity=entry['qty'],
            )

        request.session['cart'] = {}
        request.session.modified = True

        return render(request, 'order_success.html', {'order': order})

    return redirect('cart_view')


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password != password2:
            return render(request, 'register.html', {'error': 'Пароли не совпадают'})

        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'Такой пользователь уже существует'})

        user = User.objects.create_user(username=username, email=email, password=password)
        Profile.objects.create(user=user)

        login(request, user)
        return redirect('home')

    return render(request, 'register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Неверный логин или пароль'})

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('home')




@login_required
def account_view(request):
    return redirect('account_profile')


@login_required
def account_profile(request):
    profile = request.user.profile

    if request.method == 'POST':
        request.user.first_name = request.POST.get('first_name')
        request.user.last_name = request.POST.get('last_name')
        request.user.email = request.POST.get('email')
        request.user.save()

        profile.display_name = request.POST.get('display_name')
        profile.phone = request.POST.get('phone')
        profile.city = request.POST.get('city')
        profile.street = request.POST.get('street')
        profile.house = request.POST.get('house')
        profile.floor = request.POST.get('floor')
        profile.apartment = request.POST.get('apartment')
        profile.save()

        return redirect('account_profile')

    return render(request, 'account_profile.html', {'profile': profile})


@login_required
def account_orders(request):
    orders = Order.objects.filter(email=request.user.email).order_by('-created_at')

    orders_data = []
    for order in orders:
        order_items = []
        for oi in order.items.all():
            obj = None
            if oi.item_type == 'bike':
                obj = Bike.objects.filter(pk=oi.item_id).first()
            elif oi.item_type == 'part':
                obj = SparePart.objects.filter(pk=oi.item_id).first()
            elif oi.item_type == 'equipment':
                obj = Equipment.objects.filter(pk=oi.item_id).first()
            elif oi.item_type == 'accessory':
                obj = Accessory.objects.filter(pk=oi.item_id).first()
            elif oi.item_type == 'trainer':
                obj = BikeTrainer.objects.filter(pk=oi.item_id).first()

            order_items.append({
                'name': oi.item_name,
                'image': obj.image.url if obj else None,
                'quantity': oi.quantity,
                'price': oi.price,
            })

        orders_data.append({
            'order': order,
            'items': order_items,
        })

    return render(request, 'account_orders.html', {'orders_data': orders_data})


@login_required
def account_password(request):
    error = None
    success = None

    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        new_password2 = request.POST.get('new_password2')

        if not request.user.check_password(old_password):
            error = 'Текущий пароль указан неверно'
        elif new_password != new_password2:
            error = 'Новые пароли не совпадают'
        else:
            request.user.set_password(new_password)
            request.user.save()
            login(request, request.user)
            success = 'Пароль успешно изменён'

    return render(request, 'account_password.html', {'error': error, 'success': success})


@login_required
def account_wishlist(request):
    return render(request, 'account_wishlist.html')


@login_required
def toggle_wishlist_view(request, item_type, item_id):
    existing = Wishlist.objects.filter(user=request.user, item_type=item_type, item_id=item_id).first()

    if existing:
        existing.delete()
    else:
        Wishlist.objects.create(user=request.user, item_type=item_type, item_id=item_id)

    next_url = request.POST.get('next') or request.GET.get('next') or 'account_wishlist'
    return redirect(next_url)


@login_required
def account_wishlist(request):
    wishlist_qs = Wishlist.objects.filter(user=request.user).order_by('-added_at')

    items = []
    for w in wishlist_qs:
        obj = None
        detail_url = None

        if w.item_type == 'bike':
            obj = Bike.objects.filter(pk=w.item_id).first()
            detail_url = 'bike_detail'
        elif w.item_type == 'part':
            obj = SparePart.objects.filter(pk=w.item_id).first()
            detail_url = 'part_detail'
        elif w.item_type == 'equipment':
            obj = Equipment.objects.filter(pk=w.item_id).first()
            detail_url = 'equipment_detail'
        elif w.item_type == 'accessory':
            obj = Accessory.objects.filter(pk=w.item_id).first()
            detail_url = 'accessory_detail'
        elif w.item_type == 'trainer':
            obj = BikeTrainer.objects.filter(pk=w.item_id).first()
            detail_url = 'bike_trainer_detail'

        if obj:
            items.append({
                'type': w.item_type,
                'detail_url': detail_url,
                'obj': obj,
            })

    return render(request, 'account_wishlist.html', {'items': items})
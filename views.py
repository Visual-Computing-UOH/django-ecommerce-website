from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Product, Order, OrderItem, Category
from .cart import Cart
from .forms import SignUpForm


def home(request):
    categories = Category.objects.all()
    selected_category = None

    category_id = request.GET.get('category')
    if category_id:
        selected_category = get_object_or_404(Category, id=category_id)
        products = Product.objects.filter(category=selected_category)
    else:
        products = Product.objects.all()

    return render(request, 'index.html', {
        'products': products,
        'categories': categories,
        'selected_category': selected_category,
        'best_sellers': Product.objects.filter(is_best_seller=True)[:4],
        'new_arrivals': Product.objects.filter(is_new_arrival=True)[:8],
        'trending': Product.objects.filter(is_trending=True)[:8],
        'top_rated': Product.objects.filter(is_top_rated=True)[:8],
        'deals_of_day': Product.objects.filter(is_deal_of_day=True)[:2],
    })


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    related_products = Product.objects.filter(category=product.category).exclude(id=product.id)[:4]
    return render(request, 'product_detail.html', {
        'product': product,
        'related_products': related_products,
    })


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = Cart(request)
    quantity = int(request.POST.get('quantity', 1)) if request.method == 'POST' else 1
    cart.add(product=product, quantity=quantity)
    messages.success(request, f'"{product.name}" cart mein add ho gaya.')
    return redirect('cart_detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart.html', {'cart': cart})


def remove_from_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = Cart(request)
    cart.remove(product)
    messages.success(request, f'"{product.name}" cart se remove ho gaya.')
    return redirect('cart_detail')


def update_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = Cart(request)
    quantity = int(request.POST.get('quantity', 1))
    cart.update(product=product, quantity=quantity)
    return redirect('cart_detail')


def checkout(request):
    cart = Cart(request)

    if len(cart) == 0:
        messages.error(request, 'Aapka cart khali hai. Pehle products add karein.')
        return redirect('cart_detail')

    if request.method == 'POST':
        full_name = request.POST.get('full_name', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        address = request.POST.get('address', '').strip()
        city = request.POST.get('city', '').strip()

        if not all([full_name, email, phone, address, city]):
            messages.error(request, 'Sab fields fill karna zaroori hai.')
            return render(request, 'checkout.html', {'cart': cart})

        order = Order.objects.create(
            user=request.user if request.user.is_authenticated else None,
            full_name=full_name,
            email=email,
            phone=phone,
            address=address,
            city=city,
            total_price=cart.get_total_price(),
        )

        for item in cart:
            OrderItem.objects.create(
                order=order,
                product=item['product'],
                price=item['product'].price,
                quantity=item['quantity'],
            )

        cart.clear()
        return redirect('order_success', order_id=order.id)

    return render(request, 'checkout.html', {'cart': cart})


def order_success(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'order_success.html', {'order': order})


def signup_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Welcome, {user.username}! Aapka account ban gaya hai.')
            return redirect('home')
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {user.username}!')
                next_url = request.GET.get('next', 'home')
                return redirect(next_url)
        messages.error(request, 'Username ya password ghalat hai.')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.success(request, 'Aap successfully logout ho gaye hain.')
    return redirect('home')


@login_required(login_url='login')
def my_orders(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'my_orders.html', {'orders': orders})

# HOT OFFERS PAGE - jin products ka old_price set hai (discount wale)
def hot_offers(request):
    offer_products = Product.objects.filter(old_price__isnull=False)
    return render(request, 'hot_offers.html', {'products': offer_products})


# BLOG PAGE
def blog(request):
    return render(request, 'blog.html')
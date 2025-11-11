from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Product, Order, OrderItem

# Helper: check if user is admin
def is_admin(user):
    return user.is_staff

# LOGIN VIEW
def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if user.is_staff:
                return redirect("dairy:admin_dashboard")
            else:
                return redirect("dairy:shop")
        else:
            messages.error(request, "Invalid username or password")
    return render(request, "dairy/login.html")

# LOGOUT VIEW
@login_required
def user_logout(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("dairy:login")

# ADMIN DASHBOARD
@login_required
@user_passes_test(is_admin)
def admin_dashboard(request):
    products = Product.objects.all()
    orders = Order.objects.all().order_by("-created_at")
    pending_orders = orders.filter(status="PENDING")
    return render(request, "dairy/admin_dashboard.html", {
        "products": products,
        "orders": orders,
        "pending_orders": pending_orders
    })

# MANAGE PRODUCTS (Admin)
@login_required
@user_passes_test(is_admin)
def manage_products(request):
    products = Product.objects.all()
    return render(request, "dairy/manage_products.html", {"products": products})

# EDIT PRODUCT (Admin)
@login_required
@user_passes_test(is_admin)
def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        product.name = request.POST.get("name")
        product.description = request.POST.get("description")
        product.price = request.POST.get("price")
        product.stock = request.POST.get("stock")
        product.save()
        messages.success(request, "Product updated successfully.")
        return redirect("dairy:manage_products")
    return render(request, "dairy/edit_product.html", {"product": product})

# DELETE PRODUCT (Admin)
@login_required
@user_passes_test(is_admin)
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    messages.success(request, "Product deleted successfully.")
    return redirect("dairy:manage_products")

# MANAGE ORDERS (Admin)
@login_required
@user_passes_test(is_admin)
def manage_orders(request):
    orders = Order.objects.all().order_by("-created_at")
    return render(request, "dairy/manage_orders.html", {"orders": orders})

# UPDATE ORDER STATUS (Admin)
@login_required
@user_passes_test(is_admin)
def update_order_status(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == "POST":
        new_status = request.POST.get("status")
        order.status = new_status
        order.save()
        messages.success(request, "Order status updated successfully.")
    return redirect("dairy:manage_orders")

# SHOP PAGE
@login_required
def shop(request):
    products = Product.objects.filter(is_active=True)
    return render(request, "dairy/shop.html", {"products": products})

# CART SYSTEM
@login_required
def cart(request):
    cart_items = request.session.get("cart", {})
    products_qs = Product.objects.filter(pk__in=cart_items.keys())
    products_dict = {str(p.pk): p for p in products_qs}

    products = []
    total = 0
    for pk, qty in cart_items.items():
        product = products_dict.get(str(pk))
        if product:
            subtotal = product.price * qty
            total += subtotal
            products.append({"product": product, "quantity": qty, "subtotal": subtotal})

    return render(request, "dairy/cart.html", {"products": products, "total": total})

@login_required
def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    cart = request.session.get("cart", {})
    if cart.get(str(pk), 0) < product.stock:
        cart[str(pk)] = cart.get(str(pk), 0) + 1
        messages.success(request, "Product added to cart.")
    else:
        messages.error(request, "Cannot add more than available stock.")
    request.session["cart"] = cart
    return redirect("dairy:shop")

@login_required
def update_cart(request, pk):
    cart = request.session.get("cart", {})
    quantity = int(request.POST.get("quantity", 1))
    product = get_object_or_404(Product, pk=pk)
    if quantity > 0 and quantity <= product.stock:
        cart[str(pk)] = quantity
        messages.success(request, "Cart updated successfully.")
    else:
        cart.pop(str(pk), None)
        messages.success(request, "Item removed from cart.")
    request.session["cart"] = cart
    return redirect("dairy:cart")

@login_required
def remove_from_cart(request, pk):
    cart = request.session.get("cart", {})
    cart.pop(str(pk), None)
    request.session["cart"] = cart
    messages.success(request, "Item removed from cart.")
    return redirect("dairy:cart")

# CHECKOUT
@login_required
def checkout(request):
    cart = request.session.get("cart", {})
    if not cart:
        messages.error(request, "Your cart is empty.")
        return redirect("dairy:shop")

    order = Order.objects.create(customer=request.user)
    for pk, qty in cart.items():
        product = get_object_or_404(Product, pk=pk)
        OrderItem.objects.create(order=order, product=product, quantity=qty, price=product.price)
        product.stock -= qty
        product.save()

    request.session["cart"] = {}
    messages.success(request, "Order placed successfully.")
    return redirect("dairy:order_history")

# ORDER HISTORY
@login_required
def order_history(request):
    orders = Order.objects.filter(customer=request.user).order_by("-created_at")
    return render(request, "dairy/order_history.html", {"orders": orders})
# views.py

@login_required
@user_passes_test(is_admin)
def admin_dashboard(request):
    products = Product.objects.all()
    orders = Order.objects.all().order_by("-created_at")
    pending_orders = orders.filter(status="PENDING")  # Filter pending orders here
    return render(request, "dairy/admin_dashboard.html", {
        "products": products,
        "orders": orders,
        "pending_orders": pending_orders  # Pass pending orders to template
    })

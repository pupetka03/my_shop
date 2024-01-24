from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from .models import CartItem, Mobile, AppleWatch, Purchased
from django.urls import reverse
from .forms import CheckoutForm




@login_required
def add_to_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        product_type = request.POST.get('product_type')

        user = request.user
        cart_item, created = None, False

        if product_type == 'mobile':
            mobile_product = get_object_or_404(Mobile, id=product_id)
            cart_item, created = CartItem.objects.get_or_create(user=user, mobile_product=mobile_product)
        elif product_type == 'applewatch':
            watch_product = get_object_or_404(AppleWatch, id=product_id)
            cart_item, created = CartItem.objects.get_or_create(user=user, watch_product=watch_product)

        if not created:
            cart_item.quantity += 1
            cart_item.total_price = cart_item.quantity * (cart_item.mobile_product.price if cart_item.mobile_product else cart_item.watch_product.price)
            cart_item.save()

        redirect_url = request.META.get('HTTP_REFERER', '/')
        return redirect(redirect_url)

    else:
        return redirect(reverse('registration:register'))



@login_required
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    cart_total_price = sum(item.quantity * (item.mobile_product.price if item.mobile_product else item.watch_product.price) for item in cart_items)

    context = {
        'cart_items': cart_items,
        'cart_total_price': cart_total_price,
    }

    return render(request, 'cart.html', context)



@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id, user=request.user)
    cart_item.delete()
    return redirect('view_cart')



@login_required
def checkout_view(request):
    cart_items = CartItem.objects.filter(user=request.user)
    cart_total_price = sum(item.quantity * (item.mobile_product.price if item.mobile_product else item.watch_product.price) for item in cart_items)

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            purchased_order = form.save(commit=False)
            purchased_order.user = request.user
            purchased_order.products = ', '.join([f"{item.mobile_product.name} x{item.quantity}" if item.mobile_product else f"{item.watch_product.name} x{item.quantity}" for item in cart_items])
            purchased_order.total_price = cart_total_price
            purchased_order.save()

            cart_items.delete()
            
            return redirect('/products_mobile/')
    else:
        form = CheckoutForm()


    context = {
        'cart_items': cart_items,
        'cart_total_price': cart_total_price,
        'form': form,
    }

    return render(request, 'checkout.html', context)
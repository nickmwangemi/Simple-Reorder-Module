from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView

from .forms import ReorderForm, SellForm
from .models import Product, Reorder


# Create your views here.
class ProductView(ListView):
    model = Product

class ProductDetailView(DetailView):
    model = Product



def sell_product(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        form = SellForm(request.POST)
        print(form)
        if form.is_valid():
            sell_quantity = form.cleaned_data['quantity']

            product.quantity -= int(sell_quantity)
            product.save()
            messages.info(request, 'Product successfully sold')
            return redirect('store:Product Detail', product.id)
    else:
        form = SellForm()
    return render(request, 'store/sell_product.html', {'form': form, 'product': product})

def reorder_product(request, pk):
    if request.method == 'POST':
        form = ReorderForm(request.POST)
        if form.is_valid():
            reorder_quantity = form.cleaned_data['reorder_quantity']
            product = Product.objects.get(pk=pk)
            reorder = Reorder.objects.create(product=product, quantity=reorder_quantity)
            messages.info(request, 'Reorder successful')
            return redirect('Reorder Detail', reorder.id)
    else:
        form = ReorderForm()
    return render(request, 'store/reorder.html', {'form': form})

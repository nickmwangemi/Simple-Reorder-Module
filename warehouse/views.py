from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView
from store.forms import ProcessReorderForm
from store.models import Product, Reorder

# Create your views here.

class ReorderView(ListView):
    model = Reorder

class ReorderDetailView(DetailView):
    model = Reorder

def process_reorder(request, pk):
    reorder = Reorder.objects.get(pk=pk)
    product = Product.objects.get(id=reorder.product.pk)
    if request.method == 'POST':
        form = ProcessReorderForm(request.POST)
        if form.is_valid():
            process_status = form.cleaned_data['process_status']

            reorder.processed = process_status
            product_quantity_to_update = product.quantity
            reorder_quantity = reorder.quantity
            product_quantity_to_update += reorder_quantity
            product.quantity = product_quantity_to_update
            product.save()
            reorder.save()
            messages.info(request, 'Reorder processed successfully')
            return redirect('store:Product Detail', product.id)
    else:
        form = ProcessReorderForm()
    return render(request, 'warehouse/orders.html', {'form': form, 'reorder': reorder, 'product': product})

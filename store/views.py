from django.views.generic import DetailView, ListView
from .models import Product, Reorder

# Create your views here.
class ProductView(ListView):
    model = Product

class ProductDetailView(DetailView):
    model = Product

class ReorderView(ListView):
    model = Reorder

class ReorderDetailView(DetailView):
    model = Reorder
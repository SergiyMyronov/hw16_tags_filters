from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from tag_filter.models import Customer, Product, Supplier


def index(request):
    return HttpResponse("Hello, world. You're at the tag_filter index.")


def login(request):
    return HttpResponse("Log in through the admin panel")


class ProductListView(ListView):
    queryset = Product.objects.order_by('name')
    paginate_by = 30


class ProductDetailView(DetailView):
    model = Product
    fields = ['code', 'name', 'price', 'weight', 'supplier', 'description']


class ProductCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Product
    fields = ['code', 'name', 'price', 'weight', 'supplier', 'description']
    success_url = reverse_lazy('product_list')


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Product
    fields = ['code', 'name', 'price', 'weight', 'supplier', 'description']
    success_url = reverse_lazy('product_list')


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Product
    success_url = reverse_lazy('product_list')


class SupplierListView(ListView):
    queryset = Supplier.objects.order_by('name')
    paginate_by = 10


class SupplierDetailView(DetailView):
    model = Supplier
    fields = ['name', 'rating', 'city']


class SupplierCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Supplier
    fields = ['name', 'rating', 'city']
    success_url = reverse_lazy('supplier_list')


class SupplierUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Supplier
    fields = ['name', 'rating', 'city']
    success_url = reverse_lazy('supplier_list')


class SupplierDeleteView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Supplier
    success_url = reverse_lazy('supplier_list')


class CustomerListView(ListView):
    queryset = Customer.objects.order_by('name').annotate(cnt=Count('products')).prefetch_related('products')
    paginate_by = 2


class CustomerDetailView(DetailView):
    model = Customer
    fields = ['name', 'city', 'products']


class CustomerCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Customer
    fields = ['name', 'city']
    success_url = reverse_lazy('customer_list')


class CustomerUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Customer
    fields = ['name', 'city']
    success_url = reverse_lazy('customer_list')


class CustomerDeleteView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Customer
    success_url = reverse_lazy('customer_list')

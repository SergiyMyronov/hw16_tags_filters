from django.urls import path

import tag_filter.views as views

urlpatterns = [
    path('', views.index, name='index'),
    path('prod/', views.ProductListView.as_view(), name='product_list'),
    path('prod/<int:pk>', views.ProductDetailView.as_view(), name='product_detail'),
    path('prod/new', views.ProductCreateView.as_view(), name='product_form'),
    path('prod/edit/<int:pk>', views.ProductUpdateView.as_view(), name='product_form'),
    path('prod/delete/<int:pk>', views.ProductDeleteView.as_view()),
    path('supp/', views.SupplierListView.as_view(), name='supplier_list'),
    path('supp/<int:pk>', views.SupplierDetailView.as_view(), name='supplier_detail'),
    path('supp/new', views.SupplierCreateView.as_view(), name='supplier_form'),
    path('supp/edit/<int:pk>', views.SupplierUpdateView.as_view(), name='supplier_form'),
    path('supp/delete/<int:pk>', views.SupplierDeleteView.as_view()),
    path('cust/', views.CustomerListView.as_view(), name='customer_list'),
    path('cust/<int:pk>', views.CustomerDetailView.as_view(), name='customer_detail'),
    path('cust/new', views.CustomerCreateView.as_view(), name='customer_form'),
    path('cust/edit/<int:pk>', views.CustomerUpdateView.as_view(), name='customer_form'),
    path('cust/delete/<int:pk>', views.CustomerDeleteView.as_view()),
    path('login/', views.login, name='login'),
]

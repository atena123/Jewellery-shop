from django.conf.urls import url, include
from .views import all_products, product_detail, product_filter



urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^(?P<pk>\d+)/$', product_detail, name="product-detail"),
    url(r'(?P<category>\w+)/$', product_filter, name="product-filter"),
]
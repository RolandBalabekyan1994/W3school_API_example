from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from rest_framework.documentation import include_docs_urls
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title="Project Swagger")


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^docs/', include_docs_urls(title='Shop API-ներ')),
    path('Category/', include('Category.urls')),
    path('Customer/', include('Customer.urls')),
    path('Employee/', include('Employee.urls')),
    path('Order/', include('Order.urls')),
    path('OrderDetail/', include('OrderDetail.urls')),
    path('Product/', include('Product.urls')),
    path('Shipper/', include('Shipper.urls')),
    path('Supplier/', include('Supplier.urls')),
    path(r"swagger", schema_view)
]

from django.contrib import admin
from django.urls import path, include
from home.views import home_page
from createPPD import views

urlpatterns = [
    path('', home_page, name='home'),
    path('admin/', admin.site.urls),
    path('customers/', include('customers.urls')),
    path('products/',include('products.urls')),
    path('contracts/',include('contracts.urls')),
    path('createPPD', views.createPPD, name='createPPD'),
]

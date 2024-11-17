from django.urls import path
from .views import Home , Add_Product , Delete_Product , EditProduct
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('' , Home.as_view() , name = 'home'),
    path('add-product/' , Add_Product.as_view() , name = 'add-product'),
    path('delete-product/' , Delete_Product.as_view(), name='delete-product' ),
    path('edit-product/<int:id>/' , EditProduct.as_view() , name='edit-product')
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
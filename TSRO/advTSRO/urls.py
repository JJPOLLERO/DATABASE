from django.contrib import admin
from django.urls import path
from advTSRO import index 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index.webpage1, name='webpage1'),
    path('page2/', index.webpage2, name='webpage2'),
    path('page3/', index.webpage3, name='webpage3'),
    path('page4/', index.webpage4, name='webpage4'),
    path('page5/', index.webpage5, name='webpage5'),
    path('page6/', index.webpage6, name='webpage6'),
    path('delete_delivery/<int:delivery_id>/', index.delete_delivery, name='delete_delivery'),
    path('delete_product/<int:product_id>/', index.delete_product, name='delete_product'),

]

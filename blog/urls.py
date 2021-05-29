from django.urls import path
from . import views

urlpatterns = [
    path('',views.listele,name="bloglistele"), # 127.0.0.1:8000/blog/
    #   adres,views bağlantısı, link ismi
    path('detay/<int:pk>',views.gonderidetay,name="gonderidetay"), # 127.0.0.1:8000/blog/detay/1
    path('yeni/',views.yeniGonderi,name="yenigonderi"),
]

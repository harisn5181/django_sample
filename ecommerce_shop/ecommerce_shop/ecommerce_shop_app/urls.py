
from django.urls import path

from ecommerce_shop_app import views


app_name='ecommerce_shop_app'
urlpatterns = [

     path('',views.allProdCat,name="allProdCat" ),
        path('<slug:c_slug>/',views.allProdCat,name="products_by_category"),
    path('<slug:c_slug>/<slug:product_slug>/', views.proDetail, name="prodCatdetail"),
 ]





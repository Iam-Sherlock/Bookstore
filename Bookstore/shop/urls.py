from django.urls import path

from . import views

urlpatterns = [
    path("",views.home,name="ShopHome"),
    path("register",views.register,name="ShopRegister"),
    path("category",views.collection,name="categories"),
    path("category/<str:bname>",views.collectionview,name="categories"),
    path("category/<str:cname>/<str:pname>",views.product_details,name="product_details"),
]
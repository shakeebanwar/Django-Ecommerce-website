from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="HomePage"),
    path('allproduct',views.allproduct,name="allproduct"),
    path('product/<int:myid>',views.products,name="ProductView"),
    path("category/<int:cid>",views.categories,name="Master"),
    path("addtocart/<int:proid>",views.updatecart,name="updatecart"),
    path("removecart/<int:cartid>",views.removecart,name="Removecart"),
    path("signup",views.signup,name="signup"),
    path("login",views.login,name="login"),
    path('cart',views.cart,name="Cart"),
    path('logout',views.logout,name="logout"),
    path('contact',views.contact,name="contact"),
    path('tracker',views.tracker,name="tracker"),
    path('search',views.search,name="search"),
    path('checkout',views.checkout,name="Checkout"),
]
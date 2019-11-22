"""project3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, re_path

# from orders.views import CartView, SubOrderView, PizzaOrderView, PastaOrderView, SaladOrderView, DinnerOrderView, \
#     ProductDeleteView, ProductUpdateView, ConfirmationView, OrderView
# from orders import views as order_views
# from accounts.views import RegistrationView
# from pizza.views import IndexView


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    # path('logout/', LogoutView.as_view(), name='logout'),
    # path('register/', RegistrationView.as_view(), name='registration'),
    # path('order/pizza', PizzaOrderView.as_view(), name='pizza_order'),
    # path('order/sub', SubOrderView.as_view(), name='sub_order'),
    # path('order/pasta', PastaOrderView.as_view(), name='pasta_order'),
    # path('order/salad', SaladOrderView.as_view(), name='salad_order'),
    # path('order/dinner', DinnerOrderView.as_view(), name='dinner_order'),
    # path('check/price', order_views.check_price, name='check_price'),
    # path('cart', CartView.as_view(), name='cart'),
    # path('confirmation', ConfirmationView.as_view(), name='confirmation'),
    # path('orders', OrderView.as_view(), name='order_list'),
    # path('delete/<int:pk>', ProductDeleteView.as_view(), name='delete_product'),
    # path('update/<int:pk>', ProductUpdateView.as_view(), name='update_product'),
    # re_path('^$', IndexView.as_view(), name='index'),
]

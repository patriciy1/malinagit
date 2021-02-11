from django.urls import path, re_path, include
from . import views

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('dop_menu/', views.dop_menu, name='dop_menu'),
    path('dop_menu_mon/', views.dop_menu_mon, name='dop_menu_mon'),
    path('dop_menu_tue/', views.dop_menu_tue, name='dop_menu_tue'),
    path('dop_menu_wed/', views.dop_menu_wed, name='dop_menu_wed'),
    path('dop_menu_thu/', views.dop_menu_thu, name='dop_menu_thu'),
    path('dop_menu_fri/', views.dop_menu_fri, name='dop_menu_fri'),
    path('delivery/', views.delivery, name='delivery'),
    path('complex_delivery/', views.complex_delivery, name='complex_delivery'),
    path('vip_delivery/', views.vip_delivery, name='vip_delivery'),
    path('banket_delivery', views.banket_delivery, name='banket_delivery'),
    path('children_delivery/', views.children_delivery, name='children_delivery'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('checkout_cash/', views.checkout_cash, name='checkout_cash'),
    path('conditions/', views.conditions, name='conditions'),
    path('adminpanel/', views.adminpanel, name='adminpanel'),

    path('update_item/', views.updateItem, name='update_item'),
    path('process_order/', views.checkout_cash, name='checkout_cash'),
    path('', views.malina_home, name='malina_home'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
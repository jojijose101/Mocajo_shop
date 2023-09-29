from django.urls import path
from . import views

app_name='ecoshop_app'


urlpatterns = [
    path('',views.allproductcat,name='allproductcat'),
    path('<slug:c_slug>/',views.allproductcat,name='product_by_cat'),
    path('<slug:c_slug>/<slug:p_slug>',views.product,name='product_view')
]
from django.urls import path
from textiles import views
app_name = 'textiles'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('saree/', views.IndexList.as_view(), name='saree'),
    path('saree/<int:pk>/', views.saree_detail.as_view(), name='saree_detail'),
    path('cart/', views.cart_view, name='cart'),
    path('<int:pk>/buy/', views.buy_view, name='buy'),
    path('order/<int:pk>/delete/', views.OrderDelete.as_view(), name='deleteorder'),
    path('payment/', views.payment, name='payment'),
    path('response/', views.response, name='response'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('create_boutique/', views.CreateBoutique.as_view(), name='create_boutique'),
    path('create_product/', views.CreateProduct.as_view(), name='create_product'),
    path('boutiques/<int:pk>/', views.Boutique_detail.as_view(), name="boutique_detail")
    
    # path('', views.home, name='home-paytm'),
    # path('payment/', views.payment, name='payment'),
    # path('response/', views.response, name='response'),
]
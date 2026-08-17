from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('buku/', views.daftar_buku, name='daftar_buku'),
    path('buku/<int:id>/', views.detail_buku, name='detail_buku'),
    path('beli/<int:id>/', views.checkout, name='checkout'),
    path('pembayaran/<uuid:token>/', views.pembayaran, name='pembayaran'),
    path('simulasi-bayar/<uuid:token>/', views.simulasi_pembayaran, name='simulasi_pembayaran'),
    path('berhasil/<uuid:token>/', views.success, name='success'),
    path('baca/<uuid:token>/', views.baca_buku, name='baca_buku'),
]

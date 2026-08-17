from django.contrib import admin
from .models import Book, Transaction


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('judul', 'asal_cerita', 'kategori_usia', 'harga', 'berbayar', 'aktif')
    list_filter = ('berbayar', 'aktif', 'asal_cerita')
    search_fields = ('judul', 'asal_cerita')


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'book', 'nama_pembeli', 'jumlah', 'status', 'tanggal')
    list_filter = ('status', 'tanggal')
    search_fields = ('nama_pembeli', 'email', 'whatsapp', 'order_id')
    readonly_fields = ('order_id', 'access_token', 'tanggal')

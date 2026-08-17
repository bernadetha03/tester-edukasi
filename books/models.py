from django.db import models
import uuid


class Book(models.Model):
    judul = models.CharField(max_length=200)
    asal_cerita = models.CharField(max_length=100, blank=True)
    kategori_usia = models.CharField(max_length=50, blank=True)
    deskripsi = models.TextField()
    harga = models.PositiveIntegerField(default=0)
    cover = models.ImageField(upload_to='covers/', blank=True, null=True)
    preview = models.FileField(upload_to='previews/', blank=True, null=True)
    file_buku = models.FileField(upload_to='books/', blank=True, null=True)
    berbayar = models.BooleanField(default=True)
    aktif = models.BooleanField(default=True)
    tanggal_dibuat = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-tanggal_dibuat']

    def __str__(self):
        return self.judul


class Transaction(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Menunggu Pembayaran'),
        ('paid', 'Sudah Dibayar'),
        ('failed', 'Gagal'),
    ]

    book = models.ForeignKey(Book, on_delete=models.PROTECT)
    nama_pembeli = models.CharField(max_length=100)
    whatsapp = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)

    order_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    access_token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    jumlah = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    tanggal = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-tanggal']

    def __str__(self):
        return f"{self.book.judul} - {self.order_id}"

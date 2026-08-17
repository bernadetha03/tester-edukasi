# Tester Edukasi

Website edukasi dan penjualan buku cerita rakyat berbasis Django.

## Fitur
- Halaman utama
- Katalog buku
- Detail dan preview buku
- Checkout tanpa login
- Transaksi
- Simulasi pembayaran
- Akses baca menggunakan token unik
- Django Admin untuk tambah/edit buku

## Menjalankan

```bash
python -m pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Buka:
- Website: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/

## Catatan QRIS
Versi ini memakai simulasi pembayaran agar langsung bisa dites.
Untuk transaksi nyata, endpoint pembayaran perlu dihubungkan dengan payment gateway seperti Midtrans/Xendit.

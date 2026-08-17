from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from .models import Book, Transaction


def home(request):
    buku = Book.objects.filter(aktif=True)[:6]
    return render(request, 'home.html', {'buku': buku})


def daftar_buku(request):
    buku = Book.objects.filter(aktif=True)
    return render(request, 'books.html', {'buku': buku})


def detail_buku(request, id):
    buku = get_object_or_404(Book, id=id, aktif=True)
    return render(request, 'book_detail.html', {'buku': buku})


def checkout(request, id):
    buku = get_object_or_404(Book, id=id, aktif=True)

    if not buku.berbayar or buku.harga == 0:
        transaksi = Transaction.objects.create(
            book=buku,
            nama_pembeli='Pembaca Gratis',
            jumlah=0,
            status='paid'
        )
        return redirect('baca_buku', token=transaksi.access_token)

    if request.method == 'POST':
        nama = request.POST.get('nama', '').strip()
        whatsapp = request.POST.get('whatsapp', '').strip()
        email = request.POST.get('email', '').strip()

        if not nama:
            return render(request, 'checkout.html', {
                'buku': buku,
                'error': 'Nama wajib diisi.'
            })

        transaksi = Transaction.objects.create(
            book=buku,
            nama_pembeli=nama,
            whatsapp=whatsapp,
            email=email,
            jumlah=buku.harga
        )

        return redirect('pembayaran', token=transaksi.access_token)

    return render(request, 'checkout.html', {'buku': buku})


def pembayaran(request, token):
    transaksi = get_object_or_404(Transaction, access_token=token)
    return render(request, 'payment.html', {'transaksi': transaksi})


def simulasi_pembayaran(request, token):
    transaksi = get_object_or_404(Transaction, access_token=token)

    if request.method != 'POST':
        return HttpResponseForbidden("Gunakan tombol pembayaran.")

    transaksi.status = 'paid'
    transaksi.save(update_fields=['status'])

    return redirect('success', token=transaksi.access_token)


def success(request, token):
    transaksi = get_object_or_404(Transaction, access_token=token)

    if transaksi.status != 'paid':
        return redirect('pembayaran', token=token)

    return render(request, 'success.html', {'transaksi': transaksi})


def baca_buku(request, token):
    transaksi = get_object_or_404(
        Transaction.objects.select_related('book'),
        access_token=token
    )

    if transaksi.status != 'paid':
        return redirect('pembayaran', token=token)

    if not transaksi.book.file_buku:
        return render(request, 'reader.html', {
            'transaksi': transaksi,
            'buku': transaksi.book,
            'file_tidak_ada': True,
        })

    return render(request, 'reader.html', {
        'transaksi': transaksi,
        'buku': transaksi.book,
        'file_tidak_ada': False,
    })

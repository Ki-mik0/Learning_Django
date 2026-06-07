from django.shortcuts import render, redirect
from .models import Sale
from .forms import SaleForm

def sales_view(request):
    if request.method == 'POST':
        form = SaleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sales_view')
    else:
        form = SaleForm()

    sales = Sale.objects.all().order_by('-created_at')
    return render(request, 'sale/sales.html', {'sales': sales, 'form': form})
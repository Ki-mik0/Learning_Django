from django.shortcuts import render, redirect
from .forms import SalesForm
from .models import Sales

def sales_view(request):
    if request.method == 'POST':
        form = SalesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sales_view')
    else:
        form = SalesForm()


    if request.method == 'GET':
        form = SalesForm(request.GET)
        if form.is_valid():
            form.save()
            return redirect('sales_view')
    else:
        form = SalesForm()

    sales = Sales.objects.all().select_related('product').order_by('-created_at')
    return render(request, 'sales/sales.html', {'sales': sales, 'form': form})



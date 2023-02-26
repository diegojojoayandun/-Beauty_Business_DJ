from django.shortcuts import render
from django.db import connection
from ..models import Stock
from django.contrib.auth.decorators import login_required


@login_required
def all_stock(request):
    stock_available = Stock.objects.raw(
        '''select p.name_product, s.total  from products p INNER join
         stock s on p.product_id = s.product_id_id
        '''
    )
    return render(request, "management/index.html", {
        'stock_available':stock_available,
        
    })

@login_required
def stock_detail(request, name):
    stock_available = Stock.objects.raw(
        '''select p.name_product, s.total
           from products p INNER join stock s on p.product_id = s.product_id_id
           where p.name_product like  %s
        '''
    ), (name)
    return render(request, "management/index.html", {
        'stock_available':stock_available,
        
    })

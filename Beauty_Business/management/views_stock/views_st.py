from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.db.models import Count, Sum, Max
from django.db import connection
from ..models import Stock
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

@login_required
def all_stock(request, id):
    all_stock = Stock.objects.filter(id = id)
    
    return render(request, "management/index.html", {
        'stock':all_stock,
        
    })
"""
def all_supply(request, p):
    all_suply = Stock.objects.filter(p=p)
    
    return render(request, "management/index.html", {
        'stock':all_suply,
        
    })
"""
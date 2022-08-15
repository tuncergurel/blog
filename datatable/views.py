from django.shortcuts import render, HttpResponse,redirect, get_object_or_404,reverse
from django.contrib.auth.decorators import login_required

from django.db.models import Sum, F, DecimalField
from django.shortcuts import render
import pyodbc


# Create your views here.

def sqlConnect():
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=TUNCER\SQLEXPRESS01;'
                          'Database=AdventureWorks2019;'
                          'Trusted_Connection=yes;')

    cursor = conn.cursor()
    return cursor

def get_currencyList(request, *args, **kwargs):
    cur = sqlConnect()
    query = """select * from currencyList"""

    record = cur.execute(query).fetchall()

    return render(request, "get_currencyList.html", {"records": record})
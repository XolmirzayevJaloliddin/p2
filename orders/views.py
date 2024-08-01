from django.shortcuts import redirect, render
from orders.forms import OrderForm
from books.models import Book
from .models import Task


# Create your views here.
def new_order(request, pk):
    if request.method == "POST":
        form = OrderForm(request.POST) 
        if form.is_valid():
            form.save()
        else:
            print('test')
    else:
        print('get request keldi')
    return redirect ('home')


def index_view(request):
    tasks = Task.objects.all()
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print('form.errors')
    return render(request, 'index.html', {'tasks': tasks, 'form': form})
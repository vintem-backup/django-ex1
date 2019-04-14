from django.shortcuts import render, redirect, get_object_or_404
from .models import Person
from .forms import PersonForm
# Create your views here.

def persons_list(request):
    pessoas = Person.objects.all()
    return render(request, 'pessoa.html', {'var_pessoas':pessoas})

def person_new(request):
    form = PersonForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'person_form.html',{'var_form':form})

def person_update(request,id):
    pessoa = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, instance=pessoa)
    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'person_form.html',{'var_form':form})

def person_delete(request,id):
    pessoa = get_object_or_404(Person, pk=id)

    if request.method == 'POST':
        pessoa.delete()
        return redirect('person_list')

    return render(request, 'person_delete_confirm.html',{'var_pessoa':pessoa})
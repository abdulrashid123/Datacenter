
from django.shortcuts import render, redirect, get_object_or_404
from table.models import Table, Parameter
from django.db.models import Q
from django.views import generic
from django.views.generic.edit import CreateView
from .forms import ParameterForm


def code(request):
    return render(request, 'table/code.html')


class DetailView(generic.DetailView):
    model = Table
    template_name = 'table/detail.html'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['parameter'] = Parameter.objects.all()
        return context


class TableCreate(CreateView):
    model = Table
    fields = ['title']

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        return super(TableCreate, self).form_valid(form)


class ParameterCreate(CreateView):
    model = Parameter
    fields = ['parameter_title', 'unit']


def create_parameter(request, table_id):
    form = ParameterForm(request.POST or None, request.FILES or None)
    table = get_object_or_404(Table, pk=table_id)
    if form.is_valid():

        parameter = form.save(commit=False)
        parameter.table = table
        parameter.save()

        return redirect('/table/'+table_id)
    context = {
        'table': table,
        'form': form,
    }
    return render(request, 'table/create_parameter.html', context)


def delete_table(request, table_id):
    folder = Table.objects.get(pk=table_id)
    folder.delete()
    return redirect('/table')


def index(request):
    if not request.user.is_authenticated:
        return render(request, 'home/login.html')
    else:
        table = Table.objects.filter(user=request.user)
        table_results = Parameter.objects.all()
        query = request.GET.get("q")
        if query:
            table = table.filter(
                Q(title__icontains=query)

            ).distinct()
            table_results = table_results.filter(
                Q(parameter_title__icontains=query)
            ).distinct()
            return render(request, 'table/index.html', {
                'table': table,
                'parameter': table_results,
            })
        else:
            return render(request, 'table/index.html', {'table': table})





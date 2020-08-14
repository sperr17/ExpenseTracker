from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.db.models import Sum
from .forms import *


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def expenses(request):
    context = {}

    # create object of form
    form = ExpenseForm(request.POST or None)

    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        form = ExpenseForm()
        messages.success(request, "Expense successfully submitted")

    return render(request, "expenses.html", {'form': form})


def expense_chart(request):
    labels = []
    sums = []

    queryset = Expense.objects.filter(user=request.user).values('type').annotate(Sum('amount'))

    for entry in queryset:
        labels.append(entry['type'])
        sums.append(int(entry['amount__sum']))

    context = {
        'labels': labels,
        'data': sums
    }

    return render(request, "expense-chart.html", context)



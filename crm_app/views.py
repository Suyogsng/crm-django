import datetime

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.utils import timezone
from django.contrib.auth.models import Group

from django.views.generic import (
    TemplateView, View, CreateView, UpdateView, ListView, DeleteView)

from crm_app.forms import (
    LoginForm, EmployeeForm, EmployeeUpdateForm, DealForm, CustomerForm,
    EmployeeDeleteForm, ProductForm, TransactionForm)

from crm_app.models import (
    Employee, Deal, Customer, Product, Transaction)


class LoginPage(TemplateView):
    template_name = "crm_app/login.html"

    def get(self, request):
        form = LoginForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            form = LoginForm()
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/home/')
            else:
                return render(request, self.template_name, {
                    'form': form, 'user': username, 'error': 'Incorrect username or password'})


class HomePage(LoginRequiredMixin, TemplateView):
    template_name = "crm_app/home.html"


class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')


class EmployeeList(LoginRequiredMixin, ListView):
    template_name = "crm_app/employee.html"
    queryset = Employee.objects.filter(is_active=True)


class EmployeeCreate(LoginRequiredMixin, CreateView):
    template_name = "crm_app/employee_form.html"
    model = Employee
    form_class = EmployeeForm
    success_url = reverse_lazy('crm_app:home')

    def form_valid(self, form):
        password = form.cleaned_data['password']
        designation = form.cleaned_data['designation']
        employee = form.save()
        if designation.name == 'Sales and Marketing':
            grp = Group.objects.get(name='sales_and_marketings')
            employee.groups.add(grp)
        elif designation.name == 'Accounts':
            grp = Group.objects.get(name='accounts')
            employee.groups.add(grp)
        elif designation.name == 'Customer Support':
            grp = Group.objects.get(name='customer_supports')
            employee.groups.add(grp)
        elif designation.name == 'Developers':
            grp = Group.objects.get(name='developers')
            employee.groups.add(grp)
        employee.set_password(password)
        return super().form_valid(form)


class EmployeeUpdate(LoginRequiredMixin, UpdateView):
    template_name = "crm_app/employee_form.html"
    model = Employee
    form_class = EmployeeUpdateForm
    success_url = reverse_lazy('crm_app:home')

    def form_valid(self, form):
        designation = form.cleaned_data['designation']
        employee = form.save()
        if designation.name == 'Sales and Marketing':
            grp = Group.objects.get(name='sales_and_marketings')
            employee.groups.add(grp)
        elif designation.name == 'Accounts':
            grp = Group.objects.get(name='accounts')
            employee.groups.add(grp)
        elif designation.name == 'Customer Support':
            grp = Group.objects.get(name='customer_supports')
            employee.groups.add(grp)
        elif designation.name == 'Developers':
            grp = Group.objects.get(name='developers')
            employee.groups.add(grp)
        return super().form_valid(form)


class EmployeeDelete(LoginRequiredMixin, UpdateView):
    template_name = "crm_app/employee_delete.html"
    form_class = EmployeeDeleteForm
    model = Employee
    success_url = reverse_lazy("crm_app:home")

    def form_valid(self, form):
        form.instance.is_active = False
        form.save()
        return super().form_valid(form)


class DealCreate(LoginRequiredMixin, CreateView):
    template_name = "crm_app/deals form.html"
    form_class = DealForm
    model = Deal
    success_url = reverse_lazy('crm_app:deal_list')

    def form_valid(self,form):
        form.save()
        return super().form_valid(form)


class DealUpdate(LoginRequiredMixin, UpdateView):
    template_name = "crm_app/deals form.html"
    form_class = DealForm
    model = Deal
    success_url = reverse_lazy('crm_app:deal_list')

    def form_valid(self,form):
        form.save()
        return super().form_valid(form)

class DealListView(ListView):
    model = Deal

    def get_context_data(self, **kwargs):
        context = super(DealListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class DealDelete(LoginRequiredMixin, DeleteView):
    template_name = "crm_app/deal_delete.html"
    model = Deal
    success_url = reverse_lazy('crm_app:deal_list')


class CustomerView(LoginRequiredMixin, ListView):
    template_name = "crm_app/customer_list.html"
    model = Customer


class CustomerAddView(LoginRequiredMixin, View):
    template_name = 'crm_app/customer_form.html'
    def get(self, request, *args, **kwargs):
        addCustomerForm = CustomerForm()
        return render(request, self.template_name, {'form': addCustomerForm})

    def post(self, request, *args, **kwargs):
        form = CustomerForm(request.POST)
        if form.is_valid():
            albumObj = form.save(commit=False)
            albumObj.save()
            return redirect('crm_app:customer_list')

        else:
            return render(request, self.template_name, {
                'form': form, 'msg_error': "There Seems to be Some Problem. Please See Below !"})


class CustomerUpdate(LoginRequiredMixin, UpdateView):
    model = Customer
    fields = '__all__'
    success_url =  reverse_lazy('crm_app:customer_list')


class CustomerDelete(LoginRequiredMixin, DeleteView):
    model = Customer
    success_url = reverse_lazy('crm_app:customer_list')


class ProductCreate(LoginRequiredMixin, CreateView):
    template_name = "crm_app/product_form.html"
    form_class = ProductForm
    model = Product

    success_url = reverse_lazy('crm_app:product_list')

    def form_valid(self,form):
        form.save()
        return super().form_valid(form)

class ProductUpdate(LoginRequiredMixin, UpdateView):
    template_name = "crm_app/product_form.html"
    form_class = ProductForm
    model = Product

    success_url = reverse_lazy('crm_app:product_list')

    def form_valid(self,form):
        form.save()
        return super().form_valid(form)

class ProductListView(LoginRequiredMixin, ListView):
    model = Product

class ProductDelete(LoginRequiredMixin, DeleteView):
    template_name = "crm_app/product_delete.html"
    model = Product

    success_url = reverse_lazy('crm_app:product_list')


class TransactionView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = "crm_app/transaction_view.html"


class TransactionAddView(LoginRequiredMixin, View):
    template_name = 'crm_app/customer_form.html'
    def get(self, request, *args, **kwargs):
        addTransactionForm = TransactionForm()
        return render(request, self.template_name, {'form': addTransactionForm})

    def post(self, request, *args, **kwargs):
        form = TransactionForm(request.POST)
        if form.is_valid():
            albumObj = form.save(commit=False)
            albumObj.save()
            return redirect('crm_app:TrasnsctionList')

        else:
            return render(request, self.template_name, {'form': form, 'msg_error': "There Seems to be Some Problem. Please See Below !"})

class TransactionUpdate(LoginRequiredMixin, UpdateView):
    model = Transaction
    fields = '__all__'
    success_url =  reverse_lazy('crm_app:TransactionList')


class TransactionDelete(LoginRequiredMixin, DeleteView):
    model = Transaction
    success_url = reverse_lazy('crm_app:TransactionList')

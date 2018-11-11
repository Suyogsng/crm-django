from django import forms
from .models import (
    Employee, Designation, Customer, Deal, Product, Transaction)

from django.contrib.admin.widgets import AdminDateWidget


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Password'}))


class EmployeeForm(forms.ModelForm):
    designation = forms.ModelChoiceField(
        queryset=Designation.objects.all(),
        required=False,
        help_text="Select the designation(if any)",
        widget=forms.Select(
            attrs={'class': 'select form-control'}))

    class Meta:
        model = Employee
        fields = [
            'username', 'first_name', 'last_name', 'email', 'designation',
            'mobile_number', 'password'
        ]
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username',
                'required': 'True'}),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'First Name',
                'required': 'True'}),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Last Name',
                'required': 'True'}),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email',
                'required': 'True'}),
            'mobile_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Mobile Number',
                'required': 'True'}),
            'password': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Password',
                'required': 'True'}),
        }


class EmployeeUpdateForm(forms.ModelForm):
    designation = forms.ModelChoiceField(
        queryset=Designation.objects.all(),
        required=False,
        help_text="Select the designation(if any)",
        widget=forms.Select(
            attrs={'class': 'select form-control'}))

    class Meta:
        model = Employee
        fields = [
            'username', 'first_name', 'last_name', 'email', 'designation',
            'mobile_number',
        ]
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username',
                'required': 'True'}),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'First Name',
                'required': 'True'}),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Last Name',
                'required': 'True'}),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email',
                'required': 'True'}),
            'mobile_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Mobile Number',
                'required': 'True'})
        }


class EmployeeDeleteForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['is_active']
        widgets = {
            'is_active': forms.HiddenInput()
        }


class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = '__all__'


class DealForm(forms.ModelForm):
    customer = forms.ModelChoiceField(
        queryset=Customer.objects.all(),
        required=True,
        help_text="Select your company",
        widget=forms.Select(
            attrs={'class': 'select2 form-control', 'placeholder': 'Company Name'}))

    product= forms.ModelMultipleChoiceField(
        queryset=Product.objects.all(),
        required=True,
        help_text="Select products",
        widget=forms.SelectMultiple(
            attrs={'class': 'select2 form-control', 'placeholder': 'Product Title'}))
    class Meta:
        model = Deal
        fields = [
            'title', 'customer', 'start_date','end_date', 'status', 'product',
            'description', 'advance','budget'
        ]

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title',
                'required': 'True'}),

            'start_date': forms.DateInput(attrs={
                'class': 'form-control datepicker pull-right',
                'placeholder': 'Start Date',
                'required': 'True'}),
            'end_date': forms.DateInput(attrs={
                'class': 'form-control datepicker pull-right',
                'placeholder': 'End Date',
                'required': 'True'}),
            'status': forms.Select(attrs={
                'class': 'form-control select2',
                'placeholder': 'Status',
                'required': 'True'}),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Product Descritption',
                'rows': 3,
                'required': 'True'}),
            'advance': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Advance Paid',
                'required': 'True'}),
            'budget': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Total Budget',
                'required': 'True'})
        }


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = [
            'name','description'
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name',
                'required': 'True'}),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Description',
                'required': 'True'}),
                'rows': 3,
                }


class TransactionForm(forms.ModelForm):

    class Meta:
        model = Transaction
        fields = '__all__'

from django.conf.urls import url
from .views import (
    LoginPage, HomePage, LogoutView,
    EmployeeList, EmployeeCreate, EmployeeUpdate, EmployeeDelete,
    DealCreate, DealDelete, DealListView, DealUpdate,
    CustomerUpdate, CustomerView, CustomerAddView, CustomerDelete,
    ProductCreate, ProductDelete,ProductListView, ProductUpdate,
    TransactionView, TransactionAddView, TransactionUpdate, TransactionDelete)

app_name = 'crm_app'


urlpatterns = [
    url(r'^$', LoginPage.as_view(), name='login'),
    url(r'^home/$', HomePage.as_view(), name='home'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),

    url(r'^employees/$', EmployeeList.as_view(), name='employees'),
    url(r'^employee-create/$', EmployeeCreate.as_view(), name='employee_create'),
    url(r'^employee-update/(?P<pk>\d+)/$', EmployeeUpdate.as_view(), name='employee_update'),
    url(r'^employee-delete/(?P<pk>\d+)/$', EmployeeDelete.as_view(), name='employee_delete'),

    url(r'^deal_create/$', DealCreate.as_view(), name='deal_create'),
    url(r'^deal_update/(?P<pk>\d+)/$', DealUpdate.as_view(), name='deal_update'),
    url(r'^deal_list/$', DealListView.as_view(), name='deal_list'),
    url(r'^deal_delete/(?P<pk>\d+)/$', DealDelete.as_view(), name='deal_delete'),

    url(r'^customer/$', CustomerView.as_view(), name='customer_list'),
    url(r'^customer/add/$', CustomerAddView.as_view(), name='customer_create'),
    url(r'customer/update/(?P<pk>[0-9]+)/$', CustomerUpdate.as_view(), name='customer_update'),
    url(r'customer/delete/(?P<pk>[0-9]+)/$', CustomerDelete.as_view(), name='customer_delete'),

    url(r'^product_create/$', ProductCreate.as_view(), name='product_create'),
    url(r'^product_update/(?P<pk>\d+)/$', ProductUpdate.as_view(), name='product_update'),
    url(r'^product_list/$', ProductListView.as_view(), name='product_list'),
    url(r'^product_delete/(?P<pk>\d+)/$', ProductDelete.as_view(), name='product_delete'),

    url(r'^transaction/$', TransactionView.as_view(), name='TrasnsctionList'),
    url(r'^transaction/add/$', TransactionAddView.as_view(), name='TransactionAdd'),
    url(r'customer/update/(?P<pk>[0-9]+)/$', TransactionUpdate.as_view(), name='transaction_update'),
    url(r'customer/delete/(?P<pk>[0-9]+)/$', TransactionDelete.as_view(), name='transaction_delete'),

]

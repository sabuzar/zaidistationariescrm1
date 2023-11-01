from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record
from django.forms import widgets

class AddRecordForm(forms.ModelForm):
    publisher=forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"Publisher","class":"form-control"}),label="")
    book_name=forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"Book Name","class":"form-control"}),label="")
    class_name=forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"Class Name","class":"form-control"}),label="")
    price=forms.IntegerField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"Price","class":"form-control"}),label="")
    quantity=forms.IntegerField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"Quantity","class":"form-control"}),label="")
    sales=forms.IntegerField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"Sales","class":"form-control"}),label="")
    balance=forms.IntegerField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"Balance","class":"form-control"}),label="")

    class Meta:
        model=Record
        exclude=("user",)

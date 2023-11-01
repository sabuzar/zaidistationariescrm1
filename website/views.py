from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import Record
from .forms import AddRecordForm
# Create your views here.
def home(request):
    records=Record.objects.all()

    #check to see if login
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"You are logged in!!")
            return redirect('home')
        else:
            messages.success(request,"There was error logging you in please try again.......")
            return redirect('home')

    else:
        return render(request, 'home.html', {'records':records})


def logout_user(request):
    logout(request)
    messages.success(request,"You are logged out...")
    return redirect('home')

def customer_records(request,pk):
    if request.user.is_authenticated:
        customer_records=Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_records': customer_records})
    else:
        messages.success(request, "You must be logged in to view this page....")
        return redirect('home')

def delete_record(request,pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Record has been deleted succesfully....")
        return redirect('home')
    else:
        messages.success(request, "You must be logged in to delete a record....")
        return redirect('home')


def add_record(request):
    form=AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record=form.save()
                messages.success(request, "Record Added.....")
                return redirect('home')
        return render(request, 'add_record.html', {'form':form})

    else:
        messages.success(request, "You must be logged in....")
        return redirect('home')


def update_record(request,pk):
    if request.user.is_authenticated:
        current_record=Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None,instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record has been updated....")
            return redirect('home')
        return render(request, 'update_record.html', {'form': form})

    else:
        messages.success(request, "You must be logged in....")
        return redirect('home')
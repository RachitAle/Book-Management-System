from django.shortcuts import render,redirect
from django.http import HttpResponse
from.models import Book
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import BookForm


# Create your views here.

def indexview(request):
    print(request)
    print(request.method)
    print(request.GET)
    print(request.user.username)
    objs = Book.objects.all()
    forms = BookForm()
    context = {'books': objs}
    context['form'] = forms
    return render(request,'books.html',context)

@login_required
def create_book(request):

    if request.method == 'POST': 
        obj = BookForm(
            request.POST,
            request.FILES)
        
        obj.save(commit = False),
        obj.instance.user = request.user
        obj.save()
        
        return redirect('home')
        
@login_required
def update_book(request,id):
    obj = Book.objects.get(id=id)
    if request.method == "POST":
        upobj = BookForm(request.POST, request.FILES, instance = obj)
        if upobj.is_valid():
            upobj.save()
        else:
            print(upobj.errors)   
        return redirect('home')
    
    form = BookForm(instance = obj)
    context = {'form' : form, 'book' : obj} 
    return render(request, 'create_updatebooks.html',context)

@login_required
def delete_book(request, id):
    obj=Book.objects.get(id=id)
    obj.delete()
    obj=Book.objects.all()
    return redirect('home')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username,password = password)

        if user is None:
            messages.info(request,"User doesn't exists.")
            return redirect('login')

        else:
            login(request,user)
            return redirect('home') 
        
    return render(request,'login.html')
        
@login_required
def logout_view(req):
    logout(req)
    return redirect('login')
        

def signup_view(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')

        userobj = User.objects.filter(username=uname)

        if userobj.exists():
            messages.error(request, "Username already exists")
            return redirect('signup')
        
        if password == password1:
            user = User.objects.create(username=uname,email=email)
            user.set_password(password)
            user.save()
            return redirect('login')
        else:
            messages.info(request, "Password doesn't match")
            return redirect('signup')
        
    
        
    
        

    print(request.POST)
    return render(request,'signup.html')



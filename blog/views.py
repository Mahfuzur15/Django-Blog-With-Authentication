from django.shortcuts import render, redirect
from .forms import BlogCreate, RegistrationForm, UserForm, ContactForm
from .models import BlogList, Registration
# from . import forms

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.models import User  

from django.core.mail import send_mail, BadHeaderError


# Create your views here.
def index(request):
  if request.method == 'GET':
    form = ContactForm()
  else:
    form = ContactForm(request.POST)
    if form.is_valid():
      subject = form.cleaned_data['subject']
      from_email = form.cleaned_data['from_email']
      message = form.cleaned_data['message']
      try:
        send_mail(subject, message, from_email, ['admin@example.com'])
      except BadHeaderError:
        return HttpResponse('Invalid header found.')
      return HttpResponse('success')
   
  # User Registration Info 
  user_basic_info= ''
  reg_info= ''
  if request.user.is_authenticated:
    current_user = request.user
    user_id = current_user.id
    user_basic_info = User.objects.get(pk=user_id)
    reg_info = Registration.objects.filter(user__pk=user_id)
  user_basic_info = user_basic_info
  reg_info= reg_info

  if request.method == 'POST':
    fm = BlogCreate(request.POST)
    if fm.is_valid():
      fm.save()
      fm = BlogCreate()
  else:
    fm = BlogCreate()
  stud = BlogList.objects.all()
  fm = BlogCreate()  
  dict ={'cform': form, 'user_basic_info' : user_basic_info, 'reg_info': reg_info, 'form': fm, 'bloglist': stud, 'cp': 'Create New'}
  return render(request, 'base.html', context=dict)
  
  
# Delete 
def deleted(request, id):
    if request.method == 'POST':
      pi = BlogList.objects.get(pk=id)
      pi.delete()
      return HttpResponseRedirect('/')
    
def updated(request, id):
  if request.method == 'POST':
    pi = BlogList.objects.get(pk=id)
    fm = BlogCreate(request.POST, instance=pi)
    if fm.is_valid():
      fm.save()
            
    else:
      pi = BlogList.objects.get(pk=id)
      fm = BlogCreate(instance=pi)
    return render(request, 'base.html', {'form':fm, 'cp': 'Update'})
  


def register(request):
  if request.user.is_authenticated:
    return HttpResponseRedirect(reverse('index'))
  registered = False
  if request.method == 'POST':
    user_form = UserForm(request.POST)
    reg_form = RegistrationForm(request.POST)
    if reg_form.is_valid() and user_form.is_valid():
      user = user_form.save()
      user.set_password(user.password)
      user.save()
            
      user_info = reg_form.save(commit=False)
      user_info.user = user
      user_info.save()
       
      registered = True
    
  else:
      user_form = UserForm()
      reg_form = RegistrationForm()
  dict = {'user_form' : user_form, 'reg_form': reg_form, 'registered': registered}
  return render(request,'registration.html', context=dict)

def login_page(request):
  if request.user.is_authenticated:
    return HttpResponseRedirect(reverse('index'))
  return render(request,'login.html', context={})



def user_login(request):
  if request.method == 'POST':
      username = request.POST.get('username')
      password = request.POST.get('password')
        
      user = authenticate(username=username, password=password)
        
      if user:
          if user.is_active:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
                # return render(request,'index.html')
                
          else:
            return HttpResponse('Account is not Active')
      else:
        return HttpResponse('Login Details Wrong')
  else:
    return HttpResponseRedirect(reverse('login'))


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))



    


  
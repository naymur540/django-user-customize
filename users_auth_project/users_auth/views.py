from django.shortcuts import render ,redirect
from django.contrib.auth import login,authenticate,logout
from .models import *

# login function
def login_page(request):
  if request.method == 'POST':
       password=request.POST.get('password')
       username=request.POST.get('username')
       user = authenticate(request, username=username, password=password)
       if user is not None:
                login(request, user)
       return redirect('home')              
  return render(request, 'login.html')


# signup function
def signup_page(request):
  if request.method == 'POST':
    
    password=request.POST.get('password')
    confirm_password=request.POST.get('confirm_password')
    if password== confirm_password :
      CustomUserModel.objects.create_user(
        username=request.POST.get('username'),
        email=request.POST.get('email'),
        fullname=request.POST.get('fullname'),
        profile_image=request.FILES.get('profile_image'),
        grade=request.POST.get('grade'),
        passing_year=request.POST.get('passing_year'),
        institute_name=request.POST.get('institute_name'),
        last_education_name=request.POST.get('last_education_name'),
        permanent_address=request.POST.get('permanent_address'),
        present_address=request.POST.get('present_address'),
        date_of_birth=request.POST.get('date_of_birth'),
        age=request.POST.get('age'),
        gender=request.POST.get('gender'),
        mobile_number=request.POST.get('mobile_number'),
        password=password
      )
      return redirect('login')

  return render(request,"signup.html")
def logout_page(request):
    logout(request)
    return redirect('login')
def home_page(request):
     
     return render(request,"home.html")
def edit_profile(request,id):
     user = CustomUserModel.objects.get(id=id)
     if request.method == 'POST':
          user.fullname=request.POST.get('fullname')
          user.email=request.POST.get('email')
          if request.FILES.get('profile_image'):
           user.profile_image=request.FILES.get('profile_image')
          user.grade=request.POST.get('grade')
          user.passing_year=request.POST.get('passing_year')
          user.institute_name=request.POST.get('institute_name')
          user.last_education_name=request.POST.get('last_education_name')
          user.permanent_address=request.POST.get('permanent_address')
          user.present_address=request.POST.get('present_address')
          user.date_of_birth=request.POST.get('date_of_birth')
          user.age=request.POST.get('age')
          user.gender=request.POST.get('gender')
          user.mobile_number=request.POST.get('mobile_number')
          user.save()
          return redirect('home')
     return render(request,"edit_profile.html",{'user':user})
   

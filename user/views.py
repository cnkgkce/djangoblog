from django import forms
from django.core.checks.messages import Error
from django.shortcuts import redirect, render
from . import forms
# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages

import user

def register(request):
    form = forms.RegisterForm(request.POST or None) #her türlü form oluştur POSTla veya None ile 
    if form.is_valid(): #is_valid() metodunda Django arkada RegisterForm classı içinde yazdığımız clean() metodunu çağıracaktır
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        newUser = User(username = username)  #Django nun User authentication modelini kullanıyoruz
        newUser.set_password(password) #passwordu şifrei halde kaydeder
         
        newUser.save() #dbye kaydeder
        login(request,newUser)
        messages.success(request,'Başarıyla kayıt oldunuz...')
        return redirect("index") #index i name olarak vermiştik
       
    #if'e hiç girmezs yani GET request olursa ne olacka ? form oluşturup göndereceğiz

    context = {
        "form" : form
    }
    return render(request,"register.html",context)





def loginUser(request):
    form = forms.LoginForm(request.POST or None) #Eğer POST request olursa bu formdaki bilgiler doldururulur. None olursa boş döndürür
    context = {
        "form" : form
    }

    if form.is_valid(): #bu metod django içerisindeki Form.clean() metodunu çağırıyor. Bu metod default olarak zaten var ama özelleştireceksek biz bunu override ediyoruz aynı registerformda olduğu gibi 
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        tried_user = authenticate(username = username,password = password)

        if tried_user is None:
            messages.info(request,"Böyle bir kullanıcı yok")
            return render(request,"login.html",context)
        else:
            messages.success(request,"Hoş geldiniz..")
            login(request,tried_user)
            return redirect("index")

    return render(request,"login.html",context)




def logoutUser(request):
    logout(request)
    messages.success(request,"Başarıyla çıkış yaptınız...")
    return redirect("index")
from django.http import request
from django.shortcuts import render, redirect
from users.forms import RegistrationUserForm,LoginForm,ProfileCreateForm
from django.views.generic import CreateView,TemplateView
from django.contrib.auth.models import User
from users.models import Profile
from django.contrib.auth import authenticate,login,logout
# Create your views here.



class UserRegistration(TemplateView):
    form_class = RegistrationUserForm()
    template_name = "users/users_form.html"
    context = {}
    def get(self, request, *args, **kwargs):
        form = self.form_class
        self.context["form"] = form
        return render(request,self.template_name,self.context)

    def post(self, request, *args, **kwargs):
        form = RegistrationUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            self.context["form"] = form
            return render(request, self.template_name, self.context)

class user_login(TemplateView):
    model = User
    form_class = LoginForm()
    template_name = "users/users_login.html"
    context = {}
    def get(self, request, *args, **kwargs):
        form = self.form_class
        self.context["form"] = form
        return render(request,self.template_name,self.context)
    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username,password=password)
            if user:
                login(request,user)
                return redirect("home")
            else:
                return render(request,self.template_name,self.context)

        return render(request, self.template_name, self.context)

class user_home(TemplateView):
    template_name = "users/users_home.html"
    def get(self, request, *args, **kwargs):
        return render(request,self.template_name)

class ProfileCreate(TemplateView):
    model = Profile
    form_class = ProfileCreateForm()
    template_name = "users/users_create_profile.html"
    context ={}
    def get(self, request, *args, **kwargs):
        form = ProfileCreateForm(initial={"user":request.user})
        self.context["form"] = form
        return render(request,self.template_name,self.context)

    def post(self, request, *args, **kwargs):
        form = ProfileCreateForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            self.context["form"] = form
            return render(request,self.template_name,self.context)

        return render(request, self.template_name, self.context)

class view_profile(TemplateView):
    model = Profile
    template_name = "users/view_profile.html"
    context = {}
    def get(self, request, *args, **kwargs):
        user = self.model.objects.filter(user=request.user)
        self.context["users"] = user
        return render(request,self.template_name,self.context)

class edit_profile(TemplateView):
    model = Profile
    template_name = "users/edit_profile.html"
    context = {}
    def get(self, request, *args, **kwargs):
        user = self.model.objects.get(user=request.user)
        form = ProfileCreateForm(initial={"user":request.user},instance=user)
        self.context["form"] = form
        return render(request,self.template_name,self.context)

    def post(self, request, *args, **kwargs):
        user = self.model.objects.get(user=request.user)
        form = ProfileCreateForm(instance=user,data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            self.context["form"] = form
            return render(request,self.template_name,self.context)

        return render(request, self.template_name, self.context)

class user_logout(TemplateView):
    def get(self, request):
        logout(request)
        return redirect("login")

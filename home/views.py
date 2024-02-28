from django.shortcuts import render,redirect
from .forms import CreateUserForm

from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.views import LoginView,LogoutView

# Create your views here.

# def welcome(request):
    

#     context = {}

#     return render(request,'home/welcome.html',context)


'''using class based view to achieve the above'''
class HomeView(TemplateView):
    template_name = 'home/welcome.html'




# def register(request):

#     form = CreateUserForm()

#     if request.method == 'POST':
#         form = CreateUserForm(request.POST)

#         if form.is_valid():
#             form.save()
#             return redirect('login')

#         # return HttpResponseRedirect('login.html')
            
#     context = {'form':form}
#     return render(request,'home/home_signup.html',context)





'''Signup'''
class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'home/home_signup.html'
    success_url = '/db/db'

    '''make sure that only authenticated user accesses his own lists, New user to a fresh empty page'''
    def get(self,request,*args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('login')
        
        return super().get(request,*args,**kwargs)



# def login(request):

#     form = CreateUserForm()

#     context = {'form':form}

#     return render(request,'home/home_login.html', context)




'''login'''
class LoginInterfaceView(LoginView):
    template_name = 'home/home_login.html'





'''logout'''
class LogoutInterfaceView(LogoutView):
    """This view renders our logout page."""
    template_name = 'home/home_logout.html' 
    next_page = 'welcome'



    


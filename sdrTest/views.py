from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from .forms import CreateUserForm,CreateSoldierForm,AddHomeForm
from .models import Soldier,Address
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect,HttpResponse

from django.contrib import messages

from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse

# Create your views here.






# def db(request):
    
#     soldier = Soldier.objects.all()

#     context = {'soldier':soldier}

#     return render(request,'sdrTest/sdrdb.html',context)


'''display data from database using class based views'''

class SoldiersListView(LoginRequiredMixin,ListView):
    model = Soldier
    template_name = 'sdrTest/soldier_list.html'
    context_object_name = "soldiers"
    login_url = '/login'

    '''display querries of only logged in user'''

    def get_queryset(self):
        return self.request.user.soldiers.all()






def add(request):

    myform = CreateSoldierForm()

    if request.method == 'POST':
        myform = CreateSoldierForm(request.POST)

        if myform.is_valid():
            profile = myform.save(commit=False)
            profile.user = request.user
            profile.save()


            return redirect('db')

    return render(request,'sdrTest/add2.html',{'myform':myform})





def edit(request,id):

    soldier_id = int(id)

    that_soldier = Soldier.objects.get(id=soldier_id)

    edit_form = CreateSoldierForm(instance=that_soldier)


    if request.method == 'POST':

        edit_form = CreateSoldierForm(request.POST,instance=that_soldier)

        if edit_form.is_valid():
            edit_form.save()
            # messages.success(request,"Soldier updated successfully")

            return redirect('db')
        
        messages.success(request,"Soldier updated successfully")



    context = {'edit_form':edit_form}

    return render(request,'sdrTest/edit.html',context)




def deleteFunc(request,id):

    del_id = int(id)
    del_sold = Soldier.objects.get(id=del_id)
    del_sold.delete()

    return redirect('db')






def displayDetails(request,id):
    soldier_id = int(id)

    soldierDetails = Soldier.objects.get(id=soldier_id)

    # addresses = soldierDetails.address_set.all()

    context = {'soldierDetails':soldierDetails}

    return render(request,'sdrTest/details.html',context)





#adding home address


# def addHomeAddress(request):

    

#     homeForm = AddHomeForm()
    
   

#     if request.method == 'POST':
#         homeForm = AddHomeForm(request.POST)

#         if homeForm.is_valid():
#             homeForm.save()

#             address = homeForm.save(commit=False)
           
               
#             address.save()




#             return redirect('details')

#     return render(request,'sdrTest/add_homeAddress.html',{'homeForm':homeForm})



# class AddAddress(CreateView):
#     model = Address
#     form_class = AddHomeForm

#     def form_valid(self,form):

        

#         form.instance.soldier_id = self.kwargs.get('pk')
        
#         return super(AddAddress,self).form_valid(form)
    
    
    
#     def get_success_url(self):
#         return reverse('details')














#replica of the above

def addNewAddress(request,id):
    soldier_id = int(id)

    soldierDetails = Soldier.objects.get(id=soldier_id)

    # addresses = soldierDetails.address_set.all()

    addHM_form = AddHomeForm(instance=soldierDetails)


    if request.method == 'POST':
        addHM_form = AddHomeForm(request.POST)

        if addHM_form.is_valid():
        #   address = addHM_form.save(commit=False)
          addHM_form.soldier_id = addHM_form.instance
          addHM_form.soldier = addHM_form.soldier_id
          addHM_form.save()

          return redirect('db')


            



    context = {'addHM_form':addHM_form}

    return render(request,'sdrTest/address_form.html',context)






def displayAddress(request):

    return render(request,'sdrTest/homeAddress.html', {})





def displaySpouse(request):

    return render(request,'sdrTest/spouse.html', {})





def displaypNOK(request):

    return render(request,'sdrTest/pnok.html', {})





def displaysNOK(request):

    return render(request,'sdrTest/snok.html', {})






def displayEstateAdmin(request):

    return render(request,'sdrTest/estateAdmin.html', {})






def displayFormalEduc(request):

    return render(request,'sdrTest/formalEduc.html', {})







def displayMilitaryCo(request):

    return render(request,'sdrTest/militaryCourses.html', {})





def displayLivingChildren(request):

    return render(request,'sdrTest/livingChildren.html', {})


        



    # context = {'del_form':del_form}
    # return render(request,'delete.html',context)








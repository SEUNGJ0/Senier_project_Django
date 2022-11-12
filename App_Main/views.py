from django.shortcuts import render, get_object_or_404, redirect
from . models import *
from . forms import *
# 함수형 뷰에서 사용하는 권한 제한
from django.contrib.auth.decorators import login_required
# 클레스형 뷰애서 사용하는 권한 제한
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

def Main_Home(request):
    return render(request, 'Main_Home.html')

def Pet_info_View(request):
    try:
        Pet = Pet_info.objects.get(pet_owner=request.user)
    except:
        Pet = None

    try:
        Pet_diet_set = Pet_diet_set.objects.get(pet_name = Pet.pet_name)
    except:
        Pet_diet_set = None

    return render(request, 'Pet_info.html',{'Pet' : Pet, 'Pet_diet_set' : Pet_diet_set})
    
@login_required(login_url='App_Auth:login')
def Pet_create_View(request):
    if request.method == 'POST':
        form = PetForm(request.POST)
        if form.is_valid():
            Pet_info = form.save(commit=False)
            Pet_info.pet_owner = request.user
            Pet_info.save()   
            return redirect("App_Main:pet")
        context = {'form': form}
        return render(request, 'Pet_info.html',context)
    else:
        form = PetForm() # -> unboundForm

    context = {'form': form}
    return render(request, 'Pet_create.html',context)
  
@login_required(login_url='App_Auth:login')
def Pet_update_View(request):
    pet_info = get_object_or_404(Pet_info, pet_owner = request.user)
    
    if request.method == 'POST':
        form = PetForm(request.POST, instance = pet_info)
        if form.is_valid():
            print("12314")
            Pet = form.save(commit=False)
            Pet.pet_owner = request.user
            Pet.save()   
            print("1")
            return redirect("App_Main:pet")
        context = {'form': form, 'Pet' : pet_info}
        print("2")
        return render(request, 'Pet_info.html',context)
    else:
        form = PetForm(instance = pet_info) # -> unboundForm
    context = {'form': form, 'pet_info' : pet_info}
    print("3")
    return render(request, 'Pet_create.html',context)

def Pet_statistics_View(request):
    return render(request, 'Pet_statistics.html')
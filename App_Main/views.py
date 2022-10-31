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
    Pet = Pet_info.objects.get(pet_owner=request.user)
    print(Pet)
    return render(request, 'Pet_info.html',{'Pet' : Pet})

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
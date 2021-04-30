from django.shortcuts import render
from .forms import UserRegistration
# Create your views here.
def register(request) :
    if request.method=='POST' :
        form = UserRegistration(request.POST or None)
        if form.is_valid() :
            new_user= form.save(commit=False)
            new_user.set_password(
                form.cleaned_data.get('password')
            )
            new_user.save()
            return render(request,'authapp/register_done.html',{'new_user':new_user})
    else :
        form=UserRegistration()

    context={
            "form": form
        }
    return render(request,'authapp/register.html',context=context)
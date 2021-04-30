from django.shortcuts import render
from SearchDev import forms
from AddDev.models import Developer,Technology
# Create your views here.

def search_view(request):
    form=forms.SearchForm()
    if request.method=='POST':
        form=forms.SearchForm(request.POST)
        if form.is_valid() :
            print("in the is_valid section ")
            location1=form.cleaned_data['location']
            tech=form.cleaned_data['technology']
            fake=Technology.objects.get(name=tech)
            print(fake.id)
            id=fake.id
            result=Developer.objects.filter(location=location1,technology=id)

            return render(request,'SearchDev/searchresult.html',{'result':result})
    return render(request,'SearchDev/search.html',{'form':form})

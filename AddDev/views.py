from django.contrib import messages
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from AddDev.models import  Developer
from AddDev import forms



def DevloperData(request):
	developer = Developer.objects.all()
	return render(request, 'AddDev/Data.html', {'developer':developer})

def DeveloperForm(request):
	form=forms.DeveloperForm()
	if request.method=='POST' :
		form=forms.DeveloperForm(request.POST)
		if form.is_valid() :
			print("In is valid part")
			p_rating=0
			b_rating=0
			q_rating=0
			t=form.cleaned_data['project']
			for x in t :
				p_rating=x.rating
			t=form.cleaned_data['blog']
			for x in t :
				b_rating=x.rating
			t=form.cleaned_data['q_a']
			for x in t :
				q_rating=x.rating
			print("rating ",p_rating,q_rating,b_rating)
			score=gen_score(q_rating,b_rating,p_rating)
			print("score by function",score)
			form.score=score
			messages.success(request,"Developer Added Succesfully")
			print(form.cleaned_data)
			form.save()
			print("Record inserted Succesfully.....!")
			return render(request,'AddDev/thank.html')
	return render(request,'AddDev/test.html',{'form':form})

def edit_view(request,id):
	instance  =  Developer.objects.get(pk=id)
	if request.method=="POST":
		fm=forms.DeveloperForm(request.POST,instance=instance)


		if fm.is_valid:
			fm.save()
			return redirect('/home/data')
			#return redirect('AddDev/edit.html')
	fm=forms.DeveloperForm(instance=instance)
	return render(request,"AddDev/edit.html",{'fm':fm})


def gen_score(q,b,p):
	temp=(q*20 + b*30 + p*50)/100
	return temp*20

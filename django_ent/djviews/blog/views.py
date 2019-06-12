from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse,Http404, HttpResponseRedirect
from .models import PostModel
from .forms import PostModelForm
from django.db.models import Q











def post_model_robust_view(request, id= None):
	obj- None
	context={}
	success_message=' A new post was created'
	template ='detail_view.html'
	if id is None:
		templage="create_view.html"

	if id is not None:
		obj= get_object_or_404(PostModel, id=id)
		success_message='A new post was created'
		context["object"]=obj
		template="update_view.html"
		if "edit"  in request.get_full_path():
			template="update_view.html"
	if "delete" in request.get_full_path():
		template="blog/delet_view.html"
		if request.method=="POST":
			obj.delet()
			message.success(request, "Post deleted")
			return HttpResponseRedirect("/blog/")
	
	if "edit" in request.get_full_path() or "create" in request.get_full_path():
		form= PostModelForm(request.Post or None, instance=obj)
		context["form"]= form
		if form.is_valid():
			obj= form.save(commit=False)
			obj.save()
			messages.success(request, success_message)

		if obj is not None:
			return HttpResponseRedirect("/blog/{num}".format(obj.id))	
			context["form"]= PostModelForm()


	return render(request, template, context)



def post_model_create_view(request):
	# if request.method=="POST":
	# 	print (request.POST)
	# 	form= PostModelForm(request.POST)
	# 	if form.is_valid():
	# 		form.save(commit=False)
	# 		print(form.cleaned_data)

	form= PostModelForm(request.POST or None)
	context={
	"form":form
	}
	if form.is_valid():
		obj=form.save(commit=False)
		# print(form.cleaned_data)
		obj.save()
		messages.success(request, "Successfully created a form")
		return HttpResponseRedirect("/blog/{num}".format(num=obj.id))

	context={
	"form": PostModelForm()

	}
	template= "create_view.html"
	return render(request, template, context)



def post_model_update_view(request,id= None):
	obj= get_object_or_404(PostModel,id=id)
	
	form= PostModelForm(request.POST or None,instance=obj)
	context={
	"form":form,
	"object":obj
	}
	if form.is_valid():
		obj=form.save(commit=False)
		# print(form.cleaned_data)
		obj.save()
		messages.success(request, "updated post")
		return HttpResponseRedirect("/blog/{num}".format(num=obj.id))

	
	template= "update_view.html"
	return render(request, template, context)



def post_model_detail_veiw(request,id=None):
	print(id)
	# try:
	# 	obj= PostModel.objects.get(id=100)
	# except:
	# 	raise Http404
  #-----------------------------------------
	# qs= PostModel.objects.filter(id=100)
	# if no qs.exists():
	# 	raise Http404
	# else :
	# 	obj=qs.first()
 #-------------------------------------------
	obj= get_object_or_404(PostModel,id=id)

	context={
		"object":obj,
		
		}	
	
	template="detail_view.html"	



	return render(request, template, context)



def post_model_delete_view(request, id=None):
	obj= get_object_or_404(PostModel, id=id)
	if request.method=="POST":
		obj.delete()
		messages.success(request, "Post deleted")
		return HttpResponseRedirect("/blog/")
	context={
	"object": obj,
	}
	template="delete_view.html"
	return render(request, template, context)




def post_model_list_view(request):
	query=request.GET.get("q",None)
	qs= PostModel.objects.all()
	print(qs)
	#return HttpResponse("someData ")
	if query is not None:
		qs=qs.filter(Q(title__icontains= query)|
			Q(content__icontains=query)|
			Q(slug__icontains=query)
			)

	context={
		"object_list":qs,
		
		}	
	template="list_view.html"	
	return render(request,template, context)



@login_required(login_url='/login/')

def login_required_view(request):
	print(request.user)
	qs=PostModel.objects.all()
	if request.user.is_authenticated():
		print("logged in")
		template="list_view.html"
	else:
		print("Not logged in")
		template="list_view_public.html"
		#raise Http404
	
	

# Create your views here.
 
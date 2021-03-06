from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm

def home_page(request):

	context= {
	"title": "helloworld",
	"content":"welcome to the Home page"
	}
	return render(request,"home_page.html", context )

def about_page(request):
	context={
	"title": "About Page",
     "content": "welcome  to the About page"
	}
	return render(request,"home_page.html", context )

def contact_page(request):

	contact_form=ContactForm(request.POST or None )

	context= {
	"title":"contactpage",
	"content": "welcome to the Contact_page",
	"form": contact_form
	}
	if contact_form.is_valid():
		print(contact_form.cleaned_data)
	if request.method=='POST':
		#print(request.POST)

		print(request.POST.get('fullname'))
		print(request.POST.get('email'))
		print(request.POST.get('content'))

	return render(request,"contact/view.html", context )
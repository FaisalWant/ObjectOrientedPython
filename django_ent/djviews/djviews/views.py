from django.http import HttpResponse,HttpResponseRedirect


# def home(request):
# 	return HttpResponse("<h1> Hello World</h1>")

def home(request):
	response=HttpResponse()
	response.write("<p> Hey there is it me the server guy</p")
	response.write("<p> hope u had a wonderful everning</p>")
	response.status_code=200
	return (response)


def redirect_somewhere(request):
	return HttpResponseRedirect("/some/path")

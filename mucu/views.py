from django.shortcuts import render_to_response, HttpResponse 
from django.http import Http404, HttpResponseRedirect
from django.template import RequestContext
from forms import *
from models import *

def main(request):
  return render_to_response('index.html')


#method for the About Us page
def aboutUs(request):
  return render_to_response('aboutUS.html')
   
#method for the About Us page
def departments(request):
  return render_to_response('department.html') 

#method for the About Us page
def fellowships(request):
  return render_to_response('fellowships.html')

#method for the About Us page
def gallery(request):
  return render_to_response('gallery.html')

#method for the About Us page
def summons(request):
  return render_to_response('summons.html')


#method for the About Us page
def contacts(request):
  contactUs = ContactsForm()
  variables = RequestContext(request, {'contactUs': contactUs})
  return render_to_response('contacts.html', variables )


#method to save the news letter subscription
def news_letter(request):
  if request.method == "GET":
    #get the email
    e_mail = request.GET['e_mail']
    #save the email in the db
    subscriber = News_letter.objects.get_or_create(e_mail=e_mail) 
    
    #return a success message
    return HttpResponse("You have sucessfully subsribed for our monthly news!!")
    
  #request.method is not get
  else:
    return HttpResponse("Hacker!!!")


#method for the About Us page
def send_my_mail(request):
  #form = ContactsForm()
  if request.method == "GET":
    name    = request.GET["name"]
    e_mail  = request.GET["e_mail"]
    subject = request.GET["subject"]
    message = request.GET["message"]
    return HttpResponse("<em style='font-style:bold;color:blue;'>Thanks %s, your message has been received</em>"%(name))

  else:
    return HttpResponse("<em style='font-style:bold;color:red;'>An error has occured, please refresh your page and try again!!!!</em>")

from django.shortcuts import render_to_response

def main(request):

    return render_to_response('index.html')


#method for the About Us page
def aboutUs(request):
    return render_to_response('aboutUS.html')

#method for the leadership page
def leadership(request):
    return render_to_response('leadership.html')

#method for the partners page
def partners(request):
    return render_to_response('partners.html')

#method for the gallery page
def gallery(request):
    return render_to_response('gallery.html')

#method for the contacts page
def contacts(request):
	return render_to_response('contacts.html')
	
#method for the summons page
def summons(request):
	return render_to_response('summons.html')

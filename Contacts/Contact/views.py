from django.shortcuts import render, HttpResponse
from Contact.models import Person
from Contact.forms import PersonForm

# Create your views here.
def home(request):
    return render(request, 'index.html')

def html_add(request):
    return render(request, 'add_contact.html', {'form': PersonForm})

def html_add_save(request):
    # a,n,d,e,m,dp 
    adr = request.POST.get('aadhar')
    nam = request.POST.get('name')
    d = request.POST.get('dob')
    em = request.POST.get('email')
    mb = request.POST.get('mobile')
    dp = request.POST.get('dp_pic')
    try:
        Person.objects.get(aadhar=adr)
    except:
        row = Person(aadhar=adr, name=nam, dob=d, email=em, mobile=mb, dp_pic=dp)
        row.save()
        try:
            Person.objects.get(aadhar=adr)
        except:
            status = "Insert Failed"
        else:
            status = "Inserted"        
    else:
        status = "Already Existing data"
    return HttpResponse(status)
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
        #this should throw error if the aadhar is already there
        #in the DB, probably duplicate
        Person.objects.get(aadhar=adr)
    except:
        row = Person(aadhar=adr, name=nam, dob=d, email=em, mobile=mb, dp_pic=dp)
        row.save()
        try:
            #should not raise exception
            #if the above "row.save()" worked fine
            Person.objects.get(aadhar=adr)
        except:
            #this means the save failed!!
            status = "Insert Failed"
        else:
            status = "Inserted"        
    else:
        status = "Already Existing data"
    return HttpResponse(status)

def html_edit(request):
    return render(request, 'edit_contact.html', {'form': PersonForm})

def html_edit_save(request):
    edited = []
    adr = request.POST.get('aadhar')
    if adr is None:
        return HttpResponse("Aadhar is missing, mandatory to edit")
    nam = request.POST.get('name')
    d = request.POST.get('dob')
    em = request.POST.get('email')
    mb = request.POST.get('mobile')
    dp = request.POST.get('dp_pic')
    editable = nam or d or em or mb or dp
    if not editable:
        return HttpResponse("Update at least one field")
    try:
        cur = Person.objects.get(aadhar=adr)
    except:
        return HttpResponse(f"Invalid Aadhar({adr}) given")
    else:
        cols = (
            ('name', nam), ('dob', d), ('email', em),
            ('mobile', mb), ('dp_pic', dp),
        )
        for col_name, col_val in cols:
            if col_val:
                edited.append(col_name)
                eval(f"cur.{col_name} = {col_val}")
        cur.save()
    edited = ", ".join(edited)
    return HttpResponse(f"Edited {edited} for {adr}")


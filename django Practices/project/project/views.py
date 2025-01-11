from django.http import HttpResponse
from django.shortcuts import render
from service.models import Service
from contactenquirys.models import contactEnquirys



def Home(request):

    return render(request, 'index.html')

def about(request):
    
    return render(request,'about.html')

# for a in servicesData:
#     print(a.service_icon)

def service(request):
        servicesData=Service.objects.all()
        if request.method=="GET":
            st=request.GET.get('servicename')
            if st!=None:
                servicesData=Service.objects.filter(service_title__icontains=st)
        data = {
            'servicesData': servicesData

    }
        return render(request,'service.html',data)

def team(request):
    
    return render(request,'team.html')

def contact(request):
    return render(request, 'contact.html')


def saveEnguirys(request):
    if request.method == 'POST':
            name = request.POST.get("name")
            email = request.POST.get("email")
            subject = request.POST.get("subject")
            message = request.POST.get("message")
            en=contactEnquirys(name=name,email=email,subject=subject,message=message)
            en.save()
    return render(request, 'contact.html')

# def sheet(request):
#     # Initialize variables
#     t = 0
#     p = 0
#     d = None  # Initialize division variable

#     if request.method == "POST":
#         # Fetch values from form inputs
#         s1 = eval(request.POST.get("text 1"))
#         s2 = eval(request.POST.get("text 2"))
#         s3 = eval(request.POST.get("text 3"))
#         s4 = eval(request.POST.get("text 4"))
        
#         # Calculate total
#         t = s1 + s2 + s3 + s4
        
#         # Calculate percentage
#         p = t * 100 / 400
        
#         # Determine division based on percentage
#         if p >= 60:
#             d = "first div"
#         elif p >= 48:
#             d = "second div"
#         elif p >= 35:
#             d = "third div"
#         else:
#             d = "fail"
    
#     # Store all variables in a dictionary
#     context = {
#         't': t,      # Total marks
#         'p': p,      # Percentage
#         'div': d     # Division
#     }

#     # Pass the dictionary to the template
#     return render(request, 'sheet.html', context)



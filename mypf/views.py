from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
# from .models import PersonalAppContact
from .models import MDB_PersonalContact
from django.core.mail import EmailMessage
import os
import glob
import json
from django.conf import settings
# Create your views here.

def getdataAPI(request,id):
    if id==0:
        print(settings.MEDIA_ROOT+'/mypf/files/*')
        list_of_files = glob.glob(settings.MEDIA_ROOT+'/mypf/files/*')
        print(list_of_files) 
        latest_file = max(list_of_files, key=os.path.getctime)
        return printPdf(latest_file)
    elif id==1:
        return printJson(settings.MEDIA_ROOT+'/mypf/portfolio_config/config.json')
    else:
        return errorPage(request)

def errorPage(request):
    return JsonResponse({"error":404})   

def printJson(path):
    with open(settings.MEDIA_ROOT+'/mypf/portfolio_config/config.json') as FH:
        data = json.load(FH)
    return JsonResponse(data)

def printPdf(path):
  with open(path, "rb") as f:
    data = f.read()
  return HttpResponse(data, content_type='application/pdf')

# Home/Index View
def index(request):
    # check post method and request type
    if request.method == 'POST'and request.is_ajax():
        # check for empty name field
        if request.POST['name'] == "":
            username = "<Enter your name>"   #  set default name
        else:
            username = request.POST['name']
        # check for select field
        if request.POST['gender'] == "Select":
            gender = "f"
        else:
            gender = request.POST['gender']
        # return name and gender to success in ajax call top update content
        return HttpResponse(json.dumps({'name': username, 'gender': gender}))
    else:
        return render(request, 'mypf/home.html')
def tryMore(request):
    return render(request, 'mypf/tryMore.html')

#Portfolio View
def portfolio(request):
    args = {}
    args['resume_path'] = '/cdn/0/'
    with open(settings.MEDIA_ROOT+'/mypf/portfolio_config/config.json') as FH:
        data = json.load(FH)
        args['conf_data'] = data
    return render(request, 'mypf/portfolio.html', args)


# Contact View
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        form = MDB_PersonalContact(name=name, email=email, subject=subject, message=message)
        # Saving Form data to Database
        form.save_data()
                
        
        htmlBody = f'''
                <style>
                body {{
                background-image: url(https://energyart.uk/images/backgrounds/rice-paper/ricepaper-black.jpg);
                //background-repeat: no-repeat;
                background-size: cover;
                height:100%;
                background-color: black;
                padding:5px;
                }}
                </style>
                <div>
                <h1 style="text-align:center;color: lightblue;">Hi <i><span style="font-weight: bold;">{name.title}</span></i></h1>
                
                <h3 style="text-align:center;color: white;">Thanks for visiting my happy place</h3>
                
                <br>
                <h4 style="font-weight: bold;color: white;">I will get back to you soon..!</h4>
                <h4 style="font-weight: bold;color: white;">Click <a href='http://127.0.0.1:8000/'>HERE</a> to go to my happy place again.</h4>
                <br>
                <p style="color: white;">Thanks & Regards,</p>
                <p style="color: white;"><i><b>Bhavesh Itankar</b></i></p>
                
                </div>
        '''
        


        email = EmailMessage(
                'Thanks '+name.title()+', I will get back to you soon..!',
                htmlBody,
                'bhavesh.itankar@email.com', #from
                [email], #to
                ['bhavesh.itankar@email.com'] #bcc
        )
        email.content_subtype = "html"
        email.send(fail_silently=True)
        #email.send(fail_silently=False)

        return render(request, 'mypf/contact.html')
    else:
        return render(request, 'mypf/contact.html')

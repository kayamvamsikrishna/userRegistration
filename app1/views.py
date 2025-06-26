from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from app1.forms import *


def userRegistration(request):
    MUFASA=UserForm()# here i'm getting the user form object
    SIMBA=ProfileForm()#here i'm getting the profile form object
    d={'MUFASA':MUFASA,'SIMBA':SIMBA}

    if request.method=='POST' and request.FILES:
        MUFASA_FDO=UserForm(request.POST)#here i'm getting the user form obj data submitted data
        SIMBA_FDO=ProfileForm(request.POST,request.FILES)#here i'm getting the Profile form obj data submitted data (including submitted files)

        #now i need to perform validations on the submitted data
        if  MUFASA_FDO.is_valid() and SIMBA_FDO.is_valid():
            UFDO=MUFASA_FDO.save(commit=False)
            PW=MUFASA_FDO.cleaned_data['password']
            UFDO.set_password(PW)
            UFDO.save()
            #DONE

            PFDO=SIMBA_FDO.save(commit=False)
            PFDO.user=UFDO
            PFDO.save()

            #DONE

            
            send_mail('Registration',
                      'Your registration is successfull',
                      'kayamvamsikrishna@gmail.com',
                      [UFDO.email],
                      fail_silently=False)
            return HttpResponse('registration is successfull')
        
    return render(request,'h1.html',d)
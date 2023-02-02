
from django.contrib.auth import logout
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Person
from django.contrib import messages
from django.forms.models import model_to_dict




def registration_form(request):

    if request.method == "POST":
        husband_name = request.POST['husband_name']
        husband_age = request.POST['husband_age']
        husband_religion = request.POST['husband_religion']
        husband_aadhar = request.POST['husband_aadhar']

        wife_name = request.POST['wife_name']
        wife_age = request.POST['wife_age']
        wife_religion = request.POST['wife_religion']
        wife_aadhar = request.POST['wife_aadhar']

        witness_name = request.POST['witness_name']
        witness_gender = request.POST['witness_gender']
        witness_age = request.POST['witness_age']
        witness_email = request.POST['witness_email']
        witness_aadhar = request.POST['witness_aadhar']

        email = request.POST['email']
        address = request.POST['address']

        person=Person(husband_name=husband_name, husband_age=husband_age, husband_religion=husband_religion,husband_aadhar=husband_aadhar,
                      wife_name=wife_name, wife_age=wife_age, wife_religion=wife_religion, wife_aadhar=wife_aadhar,
                      witness_name=witness_name, witness_gender=witness_gender, witness_age=witness_age, witness_email=witness_email,
                      witness_aadhar=witness_aadhar, email=email,address=address )
        person.save()

        #Email essentials

        subject = "Welcome to marriage registration !"
        message = "Hello User" +"!!\n" + "Welcome to marriage registration portal!!\nThank you for visiting our website\nWe have received your registration form.\nFurther process will be undertaken by the authority, kindly have patience and co-operate.\nFurther details will be intimated to you through this mail.\n\nFor any queries write to us @ marriage.reg1617@gmail.com\nThanking you,\nRegards,\nMarriage Registration Community!"

        from_email = "marriage.reg1617@gmail.com"
        to_list = [email]
        send_mail(subject,message,from_email,to_list, fail_silently=True)





        return redirect('final_page')

    return render(request,"authentication/registration_form.html")

def final_page(request):
    return render (request,"authentication/final_page.html")



def signout(request):
    logout(request)
    messages.success(request,"Logged out successfully!")
    return redirect('home')

def edit_form(request):
    if request.method == "POST":
        husband_name = request.POST['husband_name']
        husband_age = request.POST['husband_age']
        husband_religion = request.POST['husband_religion']
        husband_aadhar = request.POST['husband_aadhar']

        wife_name = request.POST['wife_name']
        wife_age = request.POST['wife_age']
        wife_religion = request.POST['wife_religion']
        wife_aadhar = request.POST['wife_aadhar']

        witness_name = request.POST['witness_name']
        witness_gender = request.POST['witness_gender']
        witness_age = request.POST['witness_age']
        witness_email = request.POST['witness_email']
        witness_aadhar = request.POST['witness_aadhar']

        email = request.POST['email']
        address = request.POST['address']

        result = Person.objects.last()
        Person.objects.filter(id=result.id).update(husband_name=husband_name, husband_age=husband_age, husband_religion=husband_religion,
                        husband_aadhar=husband_aadhar,
                        wife_name=wife_name, wife_age=wife_age, wife_religion=wife_religion, wife_aadhar=wife_aadhar,
                        witness_name=witness_name, witness_gender=witness_gender, witness_age=witness_age,
                        witness_email=witness_email,
                        witness_aadhar=witness_aadhar, email=email, address=address)
        return redirect('final_page')
    last = model_to_dict(Person.objects.last())
    return render(request, "authentication/edit_form.html", last)



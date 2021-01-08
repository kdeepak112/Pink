from django.shortcuts import render, redirect

from .models import DoctorProfile,consultsRequest,Message,Prescription
import smtplib
from email.message import EmailMessage
import requests
from twilio.rest import Client

from datetime import *
from patient.models import patient,PatientMessage
# Create your views here.

def docHome(request):
    return render(request,'doctorHome.html')

def DocRegister(request):
    doc_user = request.POST.get('username')
    doc_email = request.POST.get('email')
    doc_phone = request.POST.get('phone')
    doc_age = request.POST.get('age')
    doc_gender = request.POST.get('gender')
    doc_password = request.POST.get('password')
    doc_experience = request.POST.get('Experience')
    doc_speciality = request.POST.get('specialisation')
    result = False
    print(doc_user)
    if DoctorProfile.objects.filter(doc_email=doc_email) or DoctorProfile.objects.filter(doc_contact=doc_phone):
        print("Already There")
        result = True
    
    if not result:
        myprod = DoctorProfile(doc_name=doc_user,doc_email=doc_email,doc_contact = doc_phone,doc_age = doc_age,doc_gender=doc_gender,doc_speciality=doc_speciality,doc_experience=doc_experience,doc_password=doc_password)
        myprod.save()
        params = {'result':"SignUp Successful"}
        sub = 'Loggin information'
        to = 'dkumardk002@gmail.com'
        body = 'This is to tell you that your  details has been noted and you would be confirmed about it in 2 hrs.You will be informed by us about the confirmation and then would be asked to send some more details and after that you can login using the same credentials please make a note of it.'
        msg = EmailMessage()
        msg.set_content(body)
        msg['subject'] = sub
        msg['to'] = to
        user = "d.ritadevi@somaiya.edu"
        msg['from'] = user
        password = "eoeuwolbvrqimzvr"
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(user, password)
        server.sendmail(user, 'dkumardk002@gmail.com', msg.as_string())
        server.quit()

        client = Client("ACc11351a484fae635f69147433d3bb99c",
                        "c90947d22f96d849fe53c0099c8bc1bc")

        client.messages.create(to="+918009978926",
                            from_="+19896629175",
                            body=body)

    else:
        params = {'result':"SignUp Unsuccessful..!! Email or Phone already registered"}

    
    return render(request,'status.html',params)  


def docLogin(request):
    result = False
    p_email = request.POST.get('email')
    p_pass = request.POST.get('password')
    if DoctorProfile.objects.filter(doc_email=p_email) and DoctorProfile.objects.filter(doc_password=p_pass):
        result = True

    if result:
        name = DoctorProfile.objects.get(doc_email=p_email)
        print(name.id)
        request.session['docuid'] = name.doc_name
        request.session['docemail'] = name.doc_email
        return redirect('docDashboard')

    else:
        params = {'result': "User Not Registered"}
        return render(request, 'status.html',params)

def docDashboard(request):
    if request.session.has_key('docemail'):
        print(request.session['docuid'])
        name = DoctorProfile.objects.get(doc_email=request.session['docemail'])
        print("Name attribute:", name.id, name.doc_email)
        params = {'username': name}
        return render(request, 'docDash.html', params)
    else:
        return redirect('docLogin')

def docLogout(request):
    print('deleting')
    del request.session['docemail']
    del request.session['docuid']
    print('deleted')
    return redirect('docHome')

def seePatient(request):
    if request.session.has_key('docemail'):
        name = DoctorProfile.objects.get(doc_email=request.session['docemail'])
        docReq = consultsRequest.objects.filter(to_doctor=name).filter(status='sent')
        params = {'patientList':docReq}
        return render(request,'seePatient.html',params)
    else:
        return redirect('docHome')

def patientConfirm(request,reqid):
    if request.session.has_key('docemail'):
        consultsRequest.objects.filter(id=reqid).update(status='accepted')
        return redirect('seePatient')
    else:
        return redirect('docHome')

def patientDelete(request,reqid):
    if request.session.has_key('docemail'):
        record = consultsRequest.objects.get(id=reqid)
        record.delete()
        return redirect('seePatient')
    else:
        return redirect('docHome')

def Docinbox(request):
    if request.session.has_key('docemail'):
        patient_list = {}
        doc = DoctorProfile.objects.get(doc_email=request.session['docemail'])
        docmsg = Message.objects.filter(to_doctor=doc).filter(status='unread')
        for i in docmsg:
            if i.from_patient.patient_name not in patient_list.keys():
                patient_list[i.from_patient.patient_name] = {}
                patient_list[i.from_patient.patient_name]['message'] = i.message
                patient_list[i.from_patient.patient_name]['count'] = 1
                patient_list[i.from_patient.patient_name]['Date'] = i.timestamp
                patient_list[i.from_patient.patient_name]['id'] = i.from_patient.id
            else:
               patient_list[i.from_patient.patient_name]['count'] += 1
               patient_list[i.from_patient.patient_name]['message'] = i.message
               patient_list[i.from_patient.patient_name]['Date'] = i.timestamp
        params = {'inbox':patient_list}
        return render(request,'inbox.html',params)
    else:
        return redirect('docHome')

def myConversations(request):
    if request.session.has_key('docemail'):
        message_list = []
        name = DoctorProfile.objects.get(doc_email=request.session['docemail'])
        docmsg = consultsRequest.objects.filter(to_doctor=name).filter(status='accepted')
        
        
        params = {'patientList':docmsg}
        return render(request,'myConversations.html',params)
    else:
        return redirect('docHome')


def Pmessage(request,pid):
    if request.session.has_key('docemail'):
        if patient.objects.filter(id=pid):
            name = patient.objects.get(id=pid)
        else:
            return redirect(myConversations)
        doc = DoctorProfile.objects.get(doc_email=request.session['docemail'])
        check =  consultsRequest.objects.filter(from_patient=name).filter(to_doctor=doc).filter(status='accepted')
        if check:
            
            Message.objects.filter(from_patient=name).filter(to_doctor=doc).update(status='read')
            docmsg = PatientMessage.objects.filter(from_doctor=doc).filter(to_patient=name)
            params = {'pid':pid,'did':doc,'docmsg':docmsg,'pname':name.patient_name,'patient':name}
            return render(request,'message.html',params)
        else:
            return redirect(myConversations)
    else:
        return redirect('docHome')

def sendMssg(request,pid):
    if request.session.has_key('docemail'):
        name = patient.objects.get(id=pid)
        doc = DoctorProfile.objects.get(doc_email=request.session['docemail'])
        doc_message = request.POST.get('Message')
        myprod = PatientMessage(to_patient = name,from_doctor=doc,message=doc_message)
        myprod.save()
        return redirect(Pmessage,pid)

def prescriptions(request):
    if request.session.has_key('docemail'):
        name = DoctorProfile.objects.get(doc_email=request.session['docemail'])
        docmsg = consultsRequest.objects.filter(to_doctor=name).filter(status='accepted')
        params = {'patientList':docmsg}
        return render(request,'uploadPrescription.html',params)
    else:
        return redirect('docHome')

def uploadPrescription(request,pid):
    if request.session.has_key('docemail'):
        name = patient.objects.get(id=pid)
        doc = DoctorProfile.objects.get(doc_email=request.session['docemail'])
        repor = request.FILES['report']
        myprod = Prescription(from_doctor=doc,to_patient=name,report=repor,timestamp=datetime.now())
        myprod.save()
        
        client = Client("ACc11351a484fae635f69147433d3bb99c",
                        "c90947d22f96d849fe53c0099c8bc1bc")

        client.messages.create(to="+918009978926",
                            from_="+19896629175",
                            body="Your Report For Test is Uploaded Please Check the reports Section")

        return redirect(prescriptions)
    else:
        return redirect('docHome')



    




   

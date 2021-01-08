from django.shortcuts import render,redirect
from django.http import HttpResponse
from patient.models import patient
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import diseaseApi , mumbai , pune , labBook , blog , PatientMessage
from .serializers import diseaseSerializer , mumbaiSerializer , puneSerializer ,labBookSerializer ,MessageSerializer,PatientMessageSerializer
import smtplib
from email.message import EmailMessage
import requests
from twilio.rest import Client
import random
from lab.models import labsRegister
from datetime import datetime  
from datetime import timedelta 
from datetime import * 
from django.core.paginator import Paginator
from doctor.models import DoctorProfile , consultsRequest , Message , Prescription


# Create your views here.


def home(request):
    return render(request, 'home.html')


def SignUp(request):
    return render(request, 'signup.html')


def login(request):
    return render(request, 'login.html')


def disease(request):
    return render(request,'disease.html')


def consult(request):
    return render(request, 'consult.html')


def covid(request):
    return render(request, 'covid.html')


def result(request):
    P_user = request.POST.get('username')
    P_email = request.POST.get('email')
    P_phone = request.POST.get('phone')
    P_age = request.POST.get('age')
    P_gender = request.POST.get('gender')
    P_password = request.POST.get('password')
    
    result = False
    print('gender:',P_gender)
    if patient.objects.filter(patient_email=P_email) and patient.objects.filter(patient_phone=P_phone):
        print("Already There")
        result = True
    
    
    if not result:
        myprod = patient(patient_name=P_user,patient_email=P_email,patient_phone=P_phone,patient_gender=P_gender,patient_age=P_age,patient_password=P_password)
        myprod.save()
        params = {'result':"SignUp Successful"}


    else:
        params = {'result':"SignUp Unsuccessful..!! Email or Phone already registered"}

    

    return render(request,'signup.html',params)    

def check(request):
    
    result = False
    p_email = request.POST.get('email')
    p_pass = request.POST.get('password')
    if patient.objects.filter(patient_email=p_email) and patient.objects.filter(patient_password=p_pass):
        result = True
        
    if result:
        name = patient.objects.get(patient_email=p_email)
        print(name.id)
        request.session['uid'] = name.patient_name
        request.session['email'] = name.patient_email
        print(request.session['uid'],request.session['email'])
        return redirect('dashboard')
    
    else:
        params = {'error':"User Not Registered"}
        return render(request,'login.html')


def dashboard(request):
    if request.session.has_key('email'):
        print(request.session['uid'])
        print(request.session['email'])
        name = patient.objects.get(patient_email=request.session['email'])
        print("Name attribute:",name.id,name.patient_email)
        params = { 'username': name}
        return render(request,'dashboard.html',params)
    else:
        return redirect('login')


def logout(request):
    print('deleting')
    del request.session['email']
    print('deleted')
    return redirect('login')

def covidInfo(request):
    if request.session.has_key('uid'):
        return render(request,'covidInfo.html')
    else:
        return render(request,'login.html')
    
    
    

def selfAssess(request):
    return render(request,'selfAssess.html')


def UserLab(request):
    return render(request,'lab.html')


def Linkupdate(request):
    if request.session.has_key('email'):
        print(request.session['uid'])
        name = patient.objects.get(patient_email=request.session['email'])
        params = { 'user': name }
        return render(request,'update.html',params)
    else:
        return render(request,'update.html')


def profile(request):
    if request.session.has_key('email'):
        print(request.session['uid'])
        print(request.session['email'])
        name = patient.objects.get(patient_email=request.session['email'])
        print("Name attribute:",name.id,name.patient_email)
        params = { 'username': name}
        return render(request,'profile.html',params)
    else:
        return redirect('login')
    

def feedback(request):
    return render(request,'feedback.html')

def update(request,userid):
    P_user = request.POST.get('username')
    P_email = request.POST.get('email')
    P_phone = request.POST.get('phone')
    P_age = request.POST.get('age')
    P_male = request.POST.get('male','off')
    P_female = request.POST.get('female','off')
    P_oldPass = request.POST.get('oldPass')
    P_password = request.POST.get('password')
    print(userid)
    name = patient.objects.get(id=userid)
    result = False
    if P_oldPass == name.patient_password:
        print(name.patient_age)
        print("already there")
        if P_user != '':
            patient.objects.filter(id=userid).update(patient_name=P_user)
            result = True
        
        if P_email != '':
            patient.objects.filter(id=userid).update(patient_email=P_email)
            result = True
        
        if P_phone != '':
            patient.objects.filter(id=userid).update(patient_phone=P_phone)
            result = True
        
        if P_age != '':
            patient.objects.filter(id=userid).update(patient_age=P_age)
            result = True

        if P_male == 'on':
            patient.objects.filter(id=userid).update(patient_gender=P_male)
            result = True

        if P_female == 'on':
            patient.objects.filter(id=userid).update(patient_gender=P_female)
            result = True

        if P_password != '':
            patient.objects.filter(id=userid).update(patient_password=P_password)
            result = True

        if result:
            params = {'status':'Updation Successful'}
        
        print(name.patient_age)
    else:
        params = {'status':'Error in updating'}
    return render(request,'update.html',params)


def book(request):
    if request.session.has_key('email'):
       
        name = patient.objects.get(patient_email=request.session['email'])
        print(request.session['email'])
        print("in book func",name.id)
        params = { 'user': name }
        return render(request,'bookLab.html',params)
    else:
        return redirect('login')
    

def bookLab(request):
    if request.session.has_key('email'):
        print('In book Lab')
        print(request.session['email'])
        name = patient.objects.get(patient_email=request.session['email'])
        print(name.id)
        
        p_id = name.id
        p_name = request.POST.get('username')
        p_email = request.POST.get('email')
        p_phone = request.POST.get('phone')
        p_age = request.POST.get('age')
        p_male = request.POST.get('male','off')
        p_female = request.POST.get('female','off')
        lab_city = request.POST.get('city')
        lab_subUrb = request.POST.get('subUrb')
        lab_name = request.POST.get('lab_name')
        test_name = request.POST.get('test')
        date = request.POST.get('date')
        time = request.POST.get('time')
        if (lab_city == '') or (lab_subUrb == '') or (lab_name == '') or (test_name == '') or (date == '') or (time == ''):
            return redirect(book)
        else:
            print(lab_name)
            lab_id = 0
            lab = labsRegister.objects.get(lab_name=lab_name)
            
            lab_id = lab.id
            
            
            p_male = 'on'
            if p_male == "on" :
                    myprod = labBook(pid = p_id,pname=p_name,pemail=p_email,pcontact=p_phone,page = p_age,pgender='male',lab_id = lab_id,lab_city=lab_city,lab_suburb=lab_subUrb,lab_name=lab_name,test_name=test_name,test_date = date,test_time = time)
                    myprod.save()
                    parms = {'status':'Booking Successful'}
            
            else:
                myprod = labBook(pid = p_id,pname=p_name,pemail=p_email,pcontact=p_phone,page = p_age,pgender='female',lab_id = lab_id,lab_city=lab_city,lab_suburb=lab_subUrb,lab_name=lab_name,test_name=test_name,test_date = date,test_time = time)
                myprod.save()

            
            print('sending message')
            sub = 'booking information'
            to = 'dkumardk002@gmail.com'
            body = 'This is to tell you that your booking has been noted and you would be confirmed about it in 2 hrs.What follows are the booking crdentials'
            msg = EmailMessage()
            msg.set_content(body)
            msg['subject'] = sub
            msg['to'] = to
            user = "d.ritadevi@somaiya.edu"
            msg['from'] = user
            password = "eoeuwolbvrqimzvr"
            server = smtplib.SMTP_SSL("smtp.gmail.com",465)
            server.login(user,password)
            server.sendmail(user,'dkumardk002@gmail.com',msg.as_string())
            server.quit()
            
            client = Client("ACc11351a484fae635f69147433d3bb99c", "c90947d22f96d849fe53c0099c8bc1bc")
            
            client.messages.create(to="+918009978926", 
                        from_="+19896629175", 
                        body="Hello from Python!")
            
            return render(request,'bookLab.html',parms)
 
   
    
    

class diseaseList(APIView):
    
    def get(self,request):
        diseaseDic = diseaseApi.objects.all()
        serializer = diseaseSerializer(diseaseDic,many=True)
        return Response(serializer.data)

class mumbaiList(APIView):
    
    def get(self,request):
        mumbaiDic = mumbai.objects.all()
        serializer = mumbaiSerializer(mumbaiDic,many=True)
        return Response(serializer.data)

class puneList(APIView):
    
    def get(self,request):
        puneDic = pune.objects.all()
        serializer = puneSerializer(puneDic,many=True)
        return Response(serializer.data)

class labBookList(APIView):
    
    def get(self,request):
        labdata = labBook.objects.all()
        serializer = labBookSerializer(labdata,many=True)
        return Response(serializer.data)


def seeBooking(request):
    if request.session.has_key('email'):
        print(request.session['uid'])
        name = patient.objects.get(patient_email=request.session['email'])
        print("Name attribute:",name.id,name.patient_email)
        record = labBook.objects.filter(pid=name.id)
        print(record)
        params = { 'record': record}
        
        return render(request,'seeBooking.html',params)
    else:
        return redirect('login')

def seeList(request):
    if request.session.has_key('email'):
        print(request.session['uid'])
        name = patient.objects.get(patient_email=request.session['email'])
        print("Name attribute:",name.id,name.patient_email)
        record = labBook.objects.filter(pid=name.id)
        print(record)
        params = { 'record': record}
        
        return render(request,'seeList.html',params)
    else:
        return redirect('login')

def forgot(request):
    return render(request,'forgot.html')

def forgotPassword(request):
    result = False
    p_email = request.POST.get('email')
    p_pass = request.POST.get('password')
    print(p_email,p_pass)
    name = patient.objects.get(patient_email=p_email) 
    if int(name.patient_phone)==int(p_pass):
        result = True
        
    if result:
        
        request.session['fgOtp'] = random.randint(1000, 5000)
        request.session['fgemail'] = name.patient_email
        print(request.session['fgOtp'],request.session['fgemail'])
        client = Client("ACc11351a484fae635f69147433d3bb99c", "c90947d22f96d849fe53c0099c8bc1bc")
        otpMsg = 'Your OTP is '+str(request.session['fgOtp'])+' and is valid for 3 minutes'
        client.messages.create(to="+918009978926", 
                       from_="+19896629175", 
                       body=otpMsg)
        request.session['otpTime'] =  datetime.now().minute
        return render(request,'otp.html')
    
    else:
        params = {'error':"User Not Registered"}
        return render(request,'forgot.html')


def otpCheck(request):
    if request.session.has_key('fgOtp'):
        print(request.session['fgOtp'])
        print(request.session['fgemail'])
        print(request.session['otpTime'])
        p_email = request.POST.get('email')
        print(p_email)
        exception = [57,58,59]
        time = (int(datetime.now().minute))-int((request.session['otpTime'])) 
        if time < 0:
            time = (time)*(-1)
            time = 60-(time)
        if (time) <= 3:
            print('inside')
            if (request.session['fgOtp']) == int(p_email):
                print('matched')
                name = patient.objects.get(patient_email=request.session['fgemail'])
                print("Name attribute:",name.id,name.patient_password)
                sub = 'Password Mail'
                to = 'dkumardk002@gmail.com'
                body = 'This is to tell you that your password has been given to you...'+name.patient_password
                msg = EmailMessage()
                msg.set_content(body)
                msg['subject'] = sub
                msg['to'] = to
                user = "d.ritadevi@somaiya.edu"
                msg['from'] = user
                password = "eoeuwolbvrqimzvr"
                server = smtplib.SMTP_SSL("smtp.gmail.com",465)
                server.login(user,password)
                server.sendmail(user,'dkumardk002@gmail.com',msg.as_string())
                server.quit()
                del request.session['fgOtp']
                del request.session['otpTime']
                params = { 'status': 'password sent to your email'}
                return render(request,'forgot.html',params)
            else:
                params = { 'status': 'Wrong OTP Entered'}
                return render(request,'forgot.html',params)
        else:
            params = { 'status': 'Time Exceeded'}
            return render(request,'forgot.html',params)
        
    
    else:
        return redirect('login')

def blogarrive(request):
    if request.session.has_key('email'):
        print(request.session['uid'])
        print(request.session['email'])
        name = patient.objects.get(patient_email=request.session['email'])
        print("Name attribute:",name.id,name.patient_email)
        params = { 'username': name}
        return render(request,'blog.html',params)
    else:
        return redirect('login')


def blogform(request):
    if request.session.has_key('email'):
        print(request.session['uid'])
        print(request.session['email'])
        name = patient.objects.get(patient_email=request.session['email'])
        print("Name attribute:",name.id,name.patient_email)
        params = { 'username': name}
        return render(request,'blogform.html',params)
    else:
        return redirect('login')

def blogEntry(request,userid):
    if request.session.has_key('email'):
        topic = request.POST.get('topic')
        desc = request.POST.get('desc')
        content = request.POST.get('content')
        
        message = ''
        
        name = patient.objects.get(patient_email=request.session['email'])
        print(name.id,userid)
        if topic == '' or desc == '' or content == '':
            message = "Empty Values Not Allowed"
            params = { 'message': message}
            return redirect(blogform)
        
        else :
            print('in here')
            if int(userid) == int(name.id):
                myprod = blog(pid = userid , topic = topic , desc = desc , content = content)
                myprod.save()
                html = blog.objects.get(pid = int(userid),topic='fg')
                print(html.content)
                params = {'topic':topic,'html':html.content}
                return render(request,'blogstatus.html',params)
    else:
        return redirect('login')

def yourBlog(request):
    if request.session.has_key('email'):
        print(request.session['uid'])
        print(request.session['email'])
        name = patient.objects.get(patient_email=request.session['email'])
        yourBlog = blog.objects.filter(pid = name.id)
        params = { 'username': name,'blog':yourBlog}
        return render(request,'yourBlog.html',params)
    else:
        return redirect('login')

def readBlog(request,blogid):
    if request.session.has_key('email'):
        print(request.session['uid'])
        print(request.session['email'])
        name = patient.objects.get(patient_email=request.session['email'])
        yourBlog = blog.objects.get(id = blogid)
        params = { 'username': name,'blog':yourBlog}
        return render(request,'readBlog.html',params)
    else:
        return redirect('login')

def allBlog(request):
    if request.session.has_key('email'):
        print(request.session['uid'])
        print(request.session['email'])
        name = patient.objects.get(patient_email=request.session['email'])
        yourBlog = blog.objects.all()
        params = { 'username': name,'blog':yourBlog}
        return render(request,'yourBlog.html',params)
    else:
        return redirect('login')


def displayDoc(request,category):
    if request.session.has_key('email'):
        print(request.session['uid'])
        print(category)
        print(request.session['email'])
        name = DoctorProfile.objects.filter(doc_speciality=category)
        pname = patient.objects.get(patient_email=request.session['email'])
        print(name)
        requestDoc = consultsRequest.objects.filter(from_patient=pname)
        print(requestDoc)
        count = len(requestDoc)
        params = { 'result': name,'requestList':requestDoc , 'category':category,'count':count}
        
        return render(request,'docDisplay.html',params)
    else:
        return redirect('login')

def sendRequest(request,doc_id,category):
    if request.session.has_key('email'):
        
        name = patient.objects.get(patient_email=request.session['email'])
        doc = DoctorProfile.objects.get(id = doc_id)
        print(name.id)
        
        myprod = consultsRequest(from_patient = name , to_doctor = doc,status='sent')
        myprod.save()
        return redirect(displayDoc,category=category)
    else:
        return redirect('login')
    

def seeRequest(request):
    if request.session.has_key('email'):
        name = patient.objects.get(patient_email=request.session['email'])
        docReq = consultsRequest.objects.filter(from_patient=name)
        params = {'docList':docReq}
        return render(request,'seeRequest.html',params)
    else:
        return redirect('login')

def Patientinbox(request):
    if request.session.has_key('email'):
        doc_list = {}
        name = patient.objects.get(patient_email=request.session['email'])
        docmsg = PatientMessage.objects.filter(to_patient=name).filter(status='unread')
        for i in docmsg:
            if i.from_doctor.doc_name not in doc_list.keys():
                doc_list[i.from_doctor.doc_name] = {}
                doc_list[i.from_doctor.doc_name]['message'] = i.message
                doc_list[i.from_doctor.doc_name]['count'] = 1
                doc_list[i.from_doctor.doc_name]['Date'] = i.timestamp
                doc_list[i.from_doctor.doc_name]['id'] = i.from_doctor.id
            else:
               doc_list[i.from_doctor.doc_name]['count'] += 1
               doc_list[i.from_doctor.doc_name]['message'] = i.message
               doc_list[i.from_doctor.doc_name]['Date'] = i.timestamp
        params = {'inbox':doc_list}
        return render(request,'patientInbox.html',params)
    else:
        return redirect('login')



class MessageList(APIView):
    
    def get(self,request):
        messageSee = Message.objects.all()
        serializer = MessageSerializer(messageSee,many=True)
        return Response(serializer.data)

class PatientMessageList(APIView):
    
    def get(self,request):
        PmessageSee = PatientMessage.objects.all()
        serializer = PatientMessageSerializer(PmessageSee,many=True)
        return Response(serializer.data)

def Dmessage(request,did):
    if request.session.has_key('email'):
        name = patient.objects.get(patient_email=request.session['email'])
        doc = DoctorProfile.objects.get(id=did)
        check =  consultsRequest.objects.filter(from_patient=name).filter(to_doctor=doc).filter(status='accepted')
        if check:
            PatientMessage.objects.filter(from_doctor=doc).filter(to_patient=name).update(status='read')
            docmsg = Message.objects.filter(from_patient=name).filter(to_doctor=doc)
            params = {'pid':name,'did':doc,'docmsg':docmsg}
            return render(request,'Pmessage.html',params)
        else:
            return redirect(myChat)
    else:
        return redirect('login')

def SendDocMssg(request):
    if request.session.has_key('email'):
        name = patient.objects.get(patient_email=request.session['email'])
        doc_message = request.POST.get('Message')
        doc_id = request.POST.get('doctorID')
        
        doc = DoctorProfile.objects.get(id=doc_id)
        myprod = Message(from_patient = name,to_doctor=doc,message=doc_message)
        myprod.save()
        return redirect(Dmessage,did=doc_id)
    else:
        return redirect('login')

def myChat(request):
    if request.session.has_key('email'):
        name = patient.objects.get(patient_email=request.session['email'])
        docReq = consultsRequest.objects.filter(from_patient=name).filter(status='accepted')
        params = {'docList':docReq}
        return render(request,'myChat.html',params)
    else:
        return redirect('login')

def antibody(request):
    if request.session.has_key('email'):
        return render(request,'antiBody.html')
    else:
        return redirect('login')

def getPrescription(request):
    if request.session.has_key('email'):
        name = patient.objects.get(patient_email=request.session['email'])
        record = Prescription.objects.filter(to_patient=name)
        print('records',record)
        params = {'record':record}
        return render(request,'getPrescription.html',params)
    else:
        return redirect('login')








   
            

    

    

    
    


        


    
 


    
        
    

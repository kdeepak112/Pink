from django.shortcuts import render, redirect
from .models import labsRegister
import smtplib
from email.message import EmailMessage
import requests
from twilio.rest import Client
from patient.models import labBook
from .filters import orderFilter
from datetime import *

test = [{'test':'Diabetes , HB','status':{
        'fasting':'no','postprandal':'no'
    },'id':None}]
# Create your views here.

def labHome(request):
    print(type(labsRegister))
    return render(request, 'labHome.html')


def labregister(request):
    print("Inside function")
    luser = request.POST.get('username')
    lemail = request.POST.get('email')
    lphone = request.POST.get('phone')
    laddress = request.POST.get('address')
    lpassword = request.POST.get('password')
    lstate = request.POST.get('state')
    ldistrict = request.POST.get('district')
    lpincode = request.POST.get('pincode')
    print(lstate,ldistrict)
    result = False

    if labsRegister.objects.filter(lab_email=lemail) and labsRegister.objects.filter(lab_contact=lphone):
        print("Already There")
        result = True

    if not result:
        myprod = labsRegister(lab_name=luser, lab_email=lemail, lab_contact=lphone, lab_address=laddress,
                              lab_password=lpassword, lab_state=lstate, lab_district=ldistrict, lab_pincode=lpincode)
        myprod.save()
        params = {'result': "SignUp Successful"}
        sub = 'booking information'
        to = 'dkumardk002@gmail.com'
        body = 'This is to tell you that your lab details has been noted and you would be confirmed about it in 2 hrs.You will be informed by us about the confirmation and then would be asked to send some more details and after that you can login using the same credentials please make a note of it.'
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
        params = {
            'result': "SignUp Unsuccessful..!! Email or Phone already registered"}
    

    return render(request, 'labHome.html',params)


def labLogin(request):
    result = False
    p_email = request.POST.get('email')
    p_pass = request.POST.get('password')
    if labsRegister.objects.filter(lab_email=p_email) and labsRegister.objects.filter(lab_password=p_pass):
        result = True

    if result:
        name = labsRegister.objects.get(lab_email=p_email)
        print(name.id)
        request.session['Labuid'] = name.lab_name
        request.session['Labemail'] = name.lab_email
        return redirect('labDashboard')

    else:
        params = {'error': "User Not Registered"}
        return render(request, 'labHome.html')


def labDashboard(request):
    if request.session.has_key('Labemail'):
        print(request.session['Labuid'])
        name = labsRegister.objects.get(lab_email=request.session['Labemail'])
        print("Name attribute:", name.id, name.lab_email)
        params = {'username': name}
        return render(request, 'labDashboard.html', params)
    else:
        return redirect('labHome')


def confirmBooking(request):
    if request.session.has_key('Labemail'):
        
        lab = labsRegister.objects.get(lab_email=request.session['Labemail'])
        print(lab.id, lab.lab_name)
        parms = labBook.objects.filter(lab_id=lab.id)
        print(parms)
        for i in parms:
            print(i.pid, i.pname, i.pcontact, i.id)
        params = {'data': parms, 'lab_id': lab.id,'test':test}
        return render(request, 'confirm.html', params)
    else:
        return redirect('labLogin')


def confirm(request, userid):
    book = labBook.objects.get(id=userid)
    labBook.objects.filter(id=userid).update(bookingStatus="yes")
    return redirect('confirmBooking')


def uploadReports(request,msg):
    if request.session.has_key('Labemail'):
        print(msg)
        lab = labsRegister.objects.get(lab_email=request.session['Labemail'])
        print(lab.id, lab.lab_name)
        parms = labBook.objects.filter(lab_id=lab.id)
        print(parms)
        for i in parms:
            print(i.pid, i.pname, i.pcontact, i.id)
        
        myFilter = orderFilter(request.GET,queryset=parms)
        parms = myFilter.qs
        params = {'data': parms, 'lab_id': lab.id,'filter':myFilter}
        
        return render(request, 'uploadReport.html', params)
    else:
        return redirect('labLogin')

def upload(request):
    book_id = request.POST.get('bookid')
    repor = request.FILES['report']
    
    up = labBook.objects.get(id=book_id)
    up.report = repor
    up.save()

    client = Client("ACc11351a484fae635f69147433d3bb99c",
                    "c90947d22f96d849fe53c0099c8bc1bc")

    client.messages.create(to="+918009978926",
                           from_="+19896629175",
                           body="Your Report For Test is Uploaded Please Check the reports Section")

    
    return redirect(uploadReports,msg='Hello')


def logoutLab(request):
    print('deleting')
    del request.session['Labemail']
    del request.session['Labuid']
    print('deleted')
    return redirect('labHome')

def userList(request):
    if request.session.has_key('Labemail'):
        print()
        lab = labsRegister.objects.get(lab_email=request.session['Labemail'])
        print(lab.id, lab.lab_name)
        parms = labBook.objects.filter(lab_id=lab.id)
        print(parms)
        for i in parms:
            print(i.pid, i.pname, i.pcontact, i.id)
        
        myFilter = orderFilter(request.GET,queryset=parms)
        parms = myFilter.qs
        params = {'data': parms, 'lab_id': lab.id,'filter':myFilter}
        
        return render(request, 'userList.html', params)
    else:
        return redirect('labLogin')

def bookingStatus(request,msg):
    if request.session.has_key('Labemail'):
        print(msg)
        test = ['Diabetes , HB','Keratin Test','gastric brushing','ascites fluid , cytology	']
        lab = labsRegister.objects.get(lab_email=request.session['Labemail'])
        todayDate = date.today()
        parms = labBook.objects.filter(lab_id=lab.id).filter(test_date = todayDate)
        params = {'data': parms,'msg':msg}
        return render(request, 'bookingStatus.html', params)
    else:
        return redirect('labLogin')

def updateBooking(request,userid,msg):
    test = ['Diabetes , HB','Keratin Test','gastric brushing','ascites fluid , cytology	']
    book = labBook.objects.get(id=userid)
    print('disease nane:',book.test_name)
    
    if book.test_name in test:
        if book.fasting == 'no':
            labBook.objects.filter(id=userid).update(fasting="yes")
            msg = "Fasting Updated of: "+book.pname
            return redirect(bookingStatus,msg=msg)
        else:
            if book.postprandal == 'no':
                msg = "Postprandal updated of: "+book.pname
                labBook.objects.filter(id=userid).update(postprandal="yes")
                labBook.objects.filter(id=userid).update(testStatus="yes")
                return redirect(bookingStatus,msg=msg)
    else:
        msg = "Booking Status of: "+book.pname+" is updated"
        labBook.objects.filter(id=userid).update(testStatus="yes")
        return redirect(bookingStatus,msg=msg)
    return redirect(bookingStatus,msg=msg)

def deleteUser(request,msg):
    if request.session.has_key('Labemail'):
        userid = id
        
        lab = labsRegister.objects.get(lab_email=request.session['Labemail'])
        print(lab.id, lab.lab_name)
        todayDate = date.today()
        print(todayDate)
        parms = labBook.objects.filter(lab_id=lab.id)
        print(parms)
        
        for i in parms:
            print(i.pid, i.pname, i.pcontact, i.id)
        
        params = {'data': parms,'msg':msg}
        
        return render(request, 'delete.html', params)
    else:
        return redirect('labLogin')

def deleteBooking(request,userid):
    book = labBook.objects.get(id=userid)
    delmsg = 'User with name: '+book.pname+' and id: '+userid+' deleted'
    book.delete()
    return redirect(deleteUser,msg=delmsg)




from django.db import models
from patient.models import patient
import datetime
# Create your models here.




class DoctorProfile(models.Model):
    
    doc_name = models.CharField(max_length=50,null=False)
    doc_age = models.SmallIntegerField(null=False)
    doc_gender = models.CharField( max_length = 10,null=False) 
    doc_email = models.CharField(max_length = 100)
    doc_contact = models.IntegerField(null=False)
    doc_speciality = models.CharField(max_length=50,null=False)
    doc_experience = models.IntegerField(null=False)
    doc_testimonials = models.TextField(max_length=5000,null=False)
    doc_achievements = models.TextField(max_length=10000,null=True)
    doc_password = models.CharField(max_length=100,null=False,default=' ')

    def __str__(self):
        return self.doc_name +' '+ self.doc_speciality

class consultsRequest(models.Model):
    from_patient = models.ForeignKey(patient,related_name='+',on_delete = models.CASCADE)
    to_doctor = models.ForeignKey(DoctorProfile,related_name='+',on_delete = models.CASCADE)
    status = models.CharField(max_length = 30,null=False,default="unsent")

    def __str__(self):
        return 'From'+' '+str(self.from_patient.id)+' to'+' '+str(self.to_doctor.id)

class Message(models.Model):
    from_patient = models.ForeignKey(patient,related_name='+',on_delete = models.CASCADE)
    to_doctor = models.ForeignKey(DoctorProfile,related_name='+',on_delete = models.CASCADE)
    message = models.TextField(max_length=10000,null=False)
    timestamp = models.DateTimeField(default=datetime.datetime.now())
    status = models.CharField(max_length=20,default='unread')


    def __str__(self):
        return 'From'+' '+str(self.from_patient.id)+' to'+' '+str(self.to_doctor.id)+'message '+self.message



class Prescription(models.Model):
    to_patient = models.ForeignKey(patient,related_name='+',on_delete = models.CASCADE)
    from_doctor = models.ForeignKey(DoctorProfile,related_name='+',on_delete = models.CASCADE)
    report = models.FileField(upload_to="prescriptions",null=True)
    timestamp = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return 'From'+' '+str(self.to_patient.id)+' to'+' '+str(self.from_doctor.id)



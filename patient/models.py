from django.db import models
import datetime

# Create your models here.


class patient(models.Model):

    patient_id = models.AutoField
    patient_image = models.ImageField(upload_to="patient/image", default="")
    patient_name = models.CharField(max_length=50)
    patient_email = models.CharField(max_length=50)
    patient_phone = models.IntegerField()
    patient_gender = models.CharField(max_length=6)
    patient_age = models.IntegerField()
    patient_password = models.CharField(max_length=20)

    def __str__(self):
        return self.patient_name


class diseaseApi(models.Model):
    advice = models.CharField(max_length=3000)
    type_disease = models.CharField(max_length=30)
    description = models.CharField(max_length=3000)

    def __str__(self):
        return self.type_disease


class mumbai(models.Model):

    lab_id = models.AutoField
    suburb_name = models.CharField(max_length=20)
    lab_name = models.CharField(max_length=50)
    test_name = models.CharField(max_length=50)
    lab_address = models.CharField(max_length=500, default="")
    cost = models.IntegerField()

    def __str__(self):
        return self.suburb_name


class ahemdabad(models.Model):

    suburb_name = models.CharField(max_length=20)
    lab_name = models.CharField(max_length=50)
    test_name = models.CharField(max_length=50)

    cost = models.IntegerField()

    def __str__(self):
        return self.suburb_name


class chennai(models.Model):

    suburb_name = models.CharField(max_length=20)
    lab_name = models.CharField(max_length=50)
    test_name = models.CharField(max_length=50)
    cost = models.IntegerField()

    def __str__(self):
        return self.suburb_name


class bengaluru(models.Model):

    suburb_name = models.CharField(max_length=20)
    lab_name = models.CharField(max_length=50)
    test_name = models.CharField(max_length=50)
    cost = models.IntegerField()

    def __str__(self):
        return self.suburb_name


class pune(models.Model):

    lab_id = models.AutoField
    suburb_name = models.CharField(max_length=20)
    lab_name = models.CharField(max_length=50)
    test_name = models.CharField(max_length=50)
    lab_address = models.CharField(max_length=500, default="")
    cost = models.IntegerField()

    def __str__(self):
        return self.suburb_name


class hyderabad(models.Model):

    suburb_name = models.CharField(max_length=20)
    lab_name = models.CharField(max_length=50)
    test_name = models.CharField(max_length=50)
    cost = models.IntegerField()

    def __str__(self):
        return self.suburb_name


class labBook(models.Model):
    book_id = models.AutoField
    pid = models.IntegerField()
    pname = models.CharField(max_length=30, null=False)
    pcontact = models.IntegerField()
    pemail = models.CharField(max_length=30, null=False)
    page = models.IntegerField()
    pgender = models.CharField(max_length=5)
    lab_id = models.IntegerField()
    lab_city = models.CharField(max_length=30, null=False)
    lab_suburb = models.CharField(max_length=30, null=False)
    lab_name = models.CharField(max_length=30, null=False)
    test_name = models.CharField(max_length=30, null=False)
    test_date = models.DateField()
    test_time = models.CharField(max_length=30, null=False)
    bookingStatus = models.CharField(max_length=5, default="No")
    testStatus = models.CharField(max_length=15, default="No")
    fasting = models.CharField(max_length=15, default="no")
    postprandal = models.CharField(max_length=15, default="no")
    report = models.FileField(null=True)


    def __str__(self):
        return self.pname



class diseaseData(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to="diseaseImage/image", default="")
    causes_symptoms = models.CharField(max_length=5000,default="")
    prevention = models.CharField(max_length=5000,default="")
    description = models.CharField(max_length=3000,default="")
    treatment = models.CharField(max_length=3000,default="")

    def __str__(self):
        return self.name

class blog(models.Model):
    pid = models.IntegerField()
    topic = models.CharField(max_length = 1000,null=False)
    desc = models.CharField(max_length = 500,null=False,default="description")
    content = models.TextField(max_length = 10000,null=False)
    timestamp = models.DateTimeField(default=datetime.datetime.now())
    def __str__(self):
        return self.topic

class PatientMessage(models.Model):
    to_patient = models.ForeignKey(patient,related_name='+',on_delete = models.CASCADE)
    from_doctor = models.ForeignKey('doctor.DoctorProfile',related_name='+',on_delete = models.CASCADE)
    message = models.TextField(max_length=10000,null=False)
    timestamp = models.DateTimeField(default=datetime.datetime.now())
    status = models.CharField(max_length=20,default='unread')


    def __str__(self):
        return 'From'+' '+str(self.from_doctor.id)+' to'+' '+str(self.to_patient.id)+'message '+self.message


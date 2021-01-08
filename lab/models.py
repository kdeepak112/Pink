from django.db import models

class labsRegister(models.Model):
    lab_id = models.AutoField
    lab_name = models.CharField(max_length = 50)
    lab_contact = models.IntegerField()
    lab_email = models.CharField(max_length = 30)
    lab_address = models.CharField(max_length = 500,default=" ")
    lab_password = models.CharField(max_length = 30,default=" ")
    lab_state = models.CharField(max_length = 15,default="")
    lab_district = models.CharField(max_length = 15,default="")
    lab_pincode = models.CharField(max_length = 6,default="")
    

    def __str__(self):
        return self.lab_name

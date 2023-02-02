from django.db import models

class Person(models.Model):
    husband_name = models.CharField(max_length=15)
    husband_age = models.CharField(max_length=15)
    husband_religion = models.CharField(max_length=15)
    husband_aadhar = models.CharField(max_length=15)



    wife_name = models.CharField(max_length=15)
    wife_age = models.CharField(max_length=15)
    wife_religion = models.CharField(max_length=15)
    wife_aadhar = models.CharField(max_length=15)



    witness_name = models.CharField(max_length=15)
    witness_gender = models.CharField(max_length=15)
    witness_age = models.CharField(max_length=15)
    witness_email = models.CharField(max_length=15)
    witness_aadhar = models.CharField(max_length=15)


    email = models.CharField(max_length=15,null=True)
    address = models.CharField(max_length=15)



from django.db import models

class Doctors(models.Model):
    Did=models.AutoField(primary_key=True)
    dname=models.CharField(max_length=100)
    diseases=models.CharField(max_length=200) 
    status=models.BooleanField(default=True)
    
    def __str__(self):
        return self.dname 

class Patient(models.Model):
    Pid=models.AutoField(primary_key=True)
    pname=models.CharField(max_length=100)
    age=models.IntegerField()
    gender=models.CharField(max_length=6)
    visiteddate=models.DateTimeField(auto_now=True)
    Did=models.ForeignKey(Doctors, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.pname 

class Prescription(models.Model):
    Prescriptionid=models.AutoField(primary_key=True)
    pname=models.ForeignKey(Patient, on_delete=models.CASCADE)
    presdate=models.DateField(auto_now=True)
    medicine=models.TextField()
    
    def __str__(self):
        return self.medicine 

class Payment(models.Model):
    Tid=models.AutoField(primary_key=True)
    medicine=models.ForeignKey(Prescription, on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.amount
    
    
    
    
    
    
    
    
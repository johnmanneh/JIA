from django.db import models

# Create your models here.
class Person(models.Modle):
    firstname       = models.CharFields(max_length=30)
    middlename      = models.CharFields(max_length=30)
    lastname        = models.CharFields(max_length=30)
    address         = models.CharFields(max_length=50)
    gender          = models.ForeignKey(Gender,on_delete=models.CASCADE)
    
class Gender(models.Model):
    gender          = [(1,' '),(2,'Male'),(3,'Female')]
    genderField     = models.CharFields(
                    max_length = 6,
                    choice = gender,
                    default = 'Null'
    )
    
class Pastors(models.Model):
    pastor          = models.ForeignKey(Person,on_delete=models.CASCADE)
    title           = models.CharFields(max_length=10)
    

class Singers(models.Model):
    singer          = models.ForeignKey(Person,on_delete=models.CASCADE)

class Band(models.Model):
    band            = models.ForeignKey(Person,on_delete=models.CASCADE)

class Ushers(models.Model):
    Ushers          = models.ForeignKey(Person,on_delete=models.CASCADE)

class Deacon(models.Model):
    deacon          = models.ForeignKey(Person,on_delete=models.CASCADE)

class PrayerRequest(models.Model):
    prayer          = models.TextField()


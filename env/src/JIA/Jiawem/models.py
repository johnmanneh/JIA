from django.db import models

# Create your models here.
class Person(models.Model):
    firstname       = models.CharField(max_length=30)
    middlename      = models.CharField(max_length=30)
    lastname        = models.CharField(max_length=30)
    address         = models.CharField(max_length=50)
    gender          = [('1',' '),('2','Male'),('3','Female')]
    genderField     = models.CharField(
                    max_length  = 6,
                    choices     = gender,
                    default     = 'null'
    )

class Pastor(models.Model):
    pastor          = models.ForeignKey(Person,on_delete=models.CASCADE)
    title           = models.CharField(max_length=10)
    

class Singer(models.Model):
    singer          = models.ForeignKey(Person,on_delete=models.CASCADE)

class Band(models.Model):
    band            = models.ForeignKey(Person,on_delete=models.CASCADE)

class Usher(models.Model):
    Ushers          = models.ForeignKey(Person,on_delete=models.CASCADE)

class Deacon(models.Model):
    deacon          = models.ForeignKey(Person,on_delete=models.CASCADE)

class PrayerRequest(models.Model):
    prayer          = models.TextField()


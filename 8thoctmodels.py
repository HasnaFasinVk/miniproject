from django.db import models

# Create your models here.
class Login(models.Model):
    usename=models.CharField(max_length=30)
    passwod=models.CharField(max_length=30)
    type=models.CharField(max_length=30)

class Registeration(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    contact=models.BigIntegerField()
    dob=models.DateField(max_length=50)
    photo=models.CharField(max_length=50)
    age=models.BigIntegerField()
    gender=models.CharField(max_length=50)
    street=models.CharField(max_length=50)
    place=models.CharField(max_length=50)
    post=models.CharField(max_length=50)
    district=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    pincode=models.IntegerField()
    height=models.CharField(max_length=50)
    weight=models.CharField(max_length=50)
    cv=models.CharField(max_length=50)
    instagramid=models.CharField(max_length=50)
    LOGIN=models.ForeignKey(Login, on_delete=models.CASCADE)

class Managecastingmain(models.Model):
    casting_film=models.CharField(max_length=100)
    producer=models.CharField(max_length=50)
    director=models.CharField(max_length=50)
    production_house=models.CharField(max_length=100)
    casting_manager=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    film_jenre=models.CharField(max_length=50)

class Managecastingsub(models.Model):
    location = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    from_date= models.DateField()
    to_date=models.DateField()
    gender=models.CharField(max_length=50)
    age_requirement = models.CharField(max_length=50)
    casting_requirements = models.CharField(max_length=500)
    video_description = models.CharField(max_length=500)
    rules = models.CharField(max_length=500)
    disablecastingstatus = models.CharField(max_length=50)
    MANAGECASTINGMAIN=models.ForeignKey(Managecastingmain,on_delete=models.CASCADE )


class Achievement(models.Model):
    date=models.DateField()
    achievements=models.CharField(max_length=500)
    certificates=models.CharField(max_length=200)
    experience=models.CharField(max_length=200)
    USER=models.ForeignKey(Registeration,  on_delete=models.CASCADE)


class Request(models.Model):
    video=models.CharField(max_length=50)
    date=models.DateField()
    status=models.CharField(max_length=50)
    CASTING=models.ForeignKey(Managecastingmain,  on_delete=models.CASCADE)
    USER=models.ForeignKey(Registeration, on_delete=models.CASCADE)


class Complaint(models.Model):
    complaint=models.CharField(max_length=300)
    reply=models.CharField(max_length=300)
    date=models.DateField()
    status=models.CharField(max_length=50)
    USER=models.ForeignKey(Registeration, on_delete=models.CASCADE)
    CASTING=models.ForeignKey(Managecastingmain, on_delete=models.CASCADE)

class Review(models.Model):
    date=models.DateField(max_length=20)
    review=models.CharField(max_length=100)
    rating=models.CharField(max_length=50)
    USER=models.ForeignKey(Registeration, on_delete=models.CASCADE)

class Selectedcandidates(models.Model):
    Description=models.CharField(max_length=100)
    date=models.DateField()
    meeting_date=models.DateField()
    venue=models.CharField(max_length=100)
    Time=models.TimeField()
    status=models.CharField(max_length=100,default="pending")
    contact=models.BigIntegerField()
    REQUEST=models.ForeignKey(Request, on_delete=models.CASCADE)

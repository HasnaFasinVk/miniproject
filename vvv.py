import datetime

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from myapp.models import *


def login(request):
    return render(request,'index.html')

def login_post(request):
    username=request.POST['name']
    password=request.POST['textfield2']

    lobj=Login.objects.filter(usename=username,passwod=password)
    if lobj.exists():
        lobj2=Login.objects.get(usename=username,passwod=password)
        request.session['lid']=lobj2.id
        if lobj2.type=='admin':
            return HttpResponse("<script>alert('Login Succesfull');window.location='/myapp/adminhome'</script>")
        elif lobj2.type=='user':
             return HttpResponse("<script>alert('Login Succesfull');window.location='/myapp/userhome/'</script>")
        else:
            return  HttpResponse("<script>alert('Invalid Login');window.location='/myapp/userhome/'</script>")

def adminhome(request):
    return render(request,'Admin/ADMIN HOME.html')



def changeps(request):
    return render(request, 'Admin/Change Password.html')
def adm_changeps_post(request):
    current_password=request.POST['textfield']
    new_password=request.POST['textfield2']
    confirm_password=request.POST['textfield3']
    cobj=Login.objects.filter(id=request.session['lid'],passwod=current_password)
    if cobj.exists():
        # cobj2=Login.objects.get(id=request.session['lid'],passwod=current_password)
        if new_password==confirm_password:
            Login.objects.filter(id=request.session['lid'],passwod=current_password).update(passwod=confirm_password)
            return HttpResponse("<script>alert('successfully changed');window.location='/myapp/login/'</script>")
        else:
            return HttpResponse("<script>alert('password missmatch');window.location='/myapp/changeps/'</script>")
    else:
        return HttpResponse("<script>alert('please check current password');window.location='/myapp/changeps/'</script>")




def approvalform(request,id):
    return render(request,'Admin/Approval Formad.html',{'id':id})

def approvalform_post(request):
    Description=request.POST['textfield']
    meeting_date=request.POST['textfield6']
    venue=request.POST['textfield5']
    time=request.POST['textfield4']
    contact=request.POST['textfield3']
    id=request.POST['id']
    obja=Selectedcandidates()
    obja.Description=Description
    obja.date=datetime.datetime.now().strftime("%Y-%m-%d")
    obja.meeting_date=meeting_date
    obja.venue=venue
    obja.Time=time
    obja.contact=contact
    obja.REQUEST_id=id
    obja.save()
    return HttpResponse("<script>alert('shared successfully');window.location='/myapp/managecastingview/'</script>")

def approvalformviewad(request,id):
    afv=Selectedcandidates.objects.filter(REQUEST__CASTING_id=id)
    return render(request,'Admin/Approval Form view.html',{'data':afv})
def approvalformviewad_post(request):
    obj15=Selectedcandidates.objects.all()
    return render(request, 'Admin/Approval Form view.html',{'data15':obj15})

def complaintreply(request,id):
    return render(request,'Admin/complaint-reply.html',{"data":id})

def complaintreply_post(request):
    reply=request.POST['textarea']
    id=request.POST['id']

    robj=Complaint.objects.get(id=id)
    robj.reply=reply
    robj.status="Replied"
    robj.save()
    return HttpResponse("<script>alert('replied');window.loction='/myapp/complaintview/'</script>")

def complaint_search(request):
    from_date=request.POST['textfield']
    to_date=request.POST['textfield2']

    crobj=Complaint.objects.filter(date__range=[from_date,to_date])
    return render(request,'Admin/Complaint-view.html',{'data':crobj})

def complaintview(request,id):
    cv=Complaint.objects.filter(CASTING_id=id)
    return render(request,'Admin/Complaint-view.html', {'data':cv})

def complaintview_post(request):
    return render(request, 'Admin/Complaint-view.html')

def emailsend(request):
    return render(request,'Admin/emailsend.html')
def emailsend_post(request):
    email=request.POST['textfield']
    description=request.POST['textarea']
    return render(request,'Admin/emailsend.html')

def managecastadd(request):
    return render(request,'Admin/manage castiing-casting call add.html')

def managecastadd_post(request):
    film_name=request.POST['textfield']
    casting_manager=request.POST['textfield8']
    email=request.POST['textfield2']
    producer=request.POST['textfield3']
    director=request.POST['textfield4']
    production_house=request.POST['textfield11']
    film_genre=request.POST['textfield10']
    location=request.POST['textfield5']
    duration=request.POST['textfield12']
    from_date=request.POST['textfield13']
    to_date=request.POST['textfield6']
    age_requirement=request.POST['textfield7']
    gender_requirement=request.POST['RadioGroup2']
    requirement_for_casting=request.POST['textarea']
    video_requirements=request.POST['textarea2']
    rules=request.POST['textfield9']

    objm= Managecastingmain()
    objm.casting_film = film_name
    objm.producer =  producer
    objm.director = director
    objm.production_house = production_house
    objm.casting_manager = casting_manager
    objm.email = email
    objm.film_jenre = film_genre
    objm.save()

    objms=Managecastingsub()
    objms.location=location
    objms.duration=duration
    objms.from_date=from_date
    objms.to_date=to_date
    objms.gender=gender_requirement
    objms.age_requirement=age_requirement
    objms.casting_requirements=requirement_for_casting
    objms.video_description=video_requirements
    objms.rules=rules
    objms.MANAGECASTINGMAIN=objm
    objms.save()
    return HttpResponse("<script>alert('casting added succesfully');window.location='/myapp/managecastingview/'</script>")

def managecastedit(request,id):
    mse=Managecastingsub.objects.get(id=id)
    return render(request,'Admin/manage casting-edit.html',{'data':mse})
def managecastedit_post(request):
    film_name = request.POST['textfield7']
    casting_manager = request.POST['casting']
    email = request.POST['textfield8']
    producer = request.POST['textfield5']
    director = request.POST['textfield4']
    production_house = request.POST['textfield9']
    film_genre = request.POST['textfield10']
    location = request.POST['textfield3']
    duration = request.POST['textfield2']
    from_date = request.POST['textfield13']
    to_date = request.POST['textfield6']
    age_requirement = request.POST['textfield']
    gender_requirement = request.POST['RadioGroup1']
    requirement_for_casting = request.POST['textarea2']
    video_requirements = request.POST['textarea']
    rules=request.POST['textfield93']
    id=request.POST['id']
    print(casting_manager,"sdfghjkl")

    objm = Managecastingmain.objects.get(id=id)
    objm.casting_film = film_name
    objm.producer = producer
    objm.director = director
    objm.production_house = production_house
    objm.casting_manager = casting_manager
    objm.email = email
    objm.film_jenre = film_genre
    objm.save()

    objms = Managecastingsub.objects.get(MANAGECASTINGMAIN_id=id)
    objms.location = location
    objms.duration = duration
    objms.from_date = from_date
    objms.to_date = to_date
    objms.gender = gender_requirement
    objms.age_requirement = age_requirement
    objms.casting_requirements = requirement_for_casting
    objms.video_description = video_requirements
    objms.rules = rules
    objms.MANAGECASTINGMAIN = objm
    objms.save()
    return HttpResponse("<script>alert('Updated');window.location='/myapp/managecastingview/'</script>")

def deletecasting(request,id):
    Managecastingsub.objects.filter(MANAGECASTINGMAIN_id=id).delete()
    Managecastingmain.objects.filter(id=id).delete()
    return HttpResponse("<script>alert('Updated');window.location='/myapp/managecastingview/'</script>")




def filmsearch(request):
    casting_film=request.POST['textfields']
    objmv=Managecastingsub.objects.filter(MANAGECASTINGMAIN__casting_film__icontains=casting_film)
    return render(request, 'Admin/manage casting-view.html',{'datamv':objmv})

def managecastingview(request):
    objmv=Managecastingsub.objects.all()
    return render(request,'Admin/manage casting-view.html',{'datamv':objmv})

def managecastingview_post(request):
    obj=Managecastingsub.objects.all()
    return render(request, 'Admin/manage casting-view.html',{"data":obj})


def reviewsearch(request):
    from_date=request.POST['textfield']
    to_date=request.POST['textfield2']
    rsr= Review.objects.filter(date__range=[from_date,to_date])
    return render(request,'Admin/Review view.html', {'data6':rsr})

def reviewview(request):
    objrv=Review.objects.all()
    return render(request,'Admin/Review view.html',{'data6':objrv})
def reviewview_post(request):
    return render(request, 'Admin/Review view.html')


def selecandidatesearch(request):
    from_date=request.POST['textfield']
    to_date=request.POST['textfield2']
    return render(request, 'Admin/Selected candidates VIEW.html')
def selectedcandidates(request,id):
    sc=Request.objects.filter(status="Approved",CASTING_id=id)
    return render(request,'Admin/Selected candidates VIEW.html',{'data':sc})
def selectedcandidates_post(request):
    from_date = request.POST['textfield']
    to_date = request.POST['textfield2']
    obj1=Request.objects.filter(status='Approved',date__range=[from_date,to_date])
    return render(request, 'Admin/Selected candidates VIEW.html',{'data1':obj1})

def userdetailview(request,id):
    uda=Achievement.objects.filter(USER_id=id)
    udv = Registeration.objects.get(id=id)

    return render(request,'Admin/User details view.html',{'data2':uda,'data':udv})
def userdetailview_post(request):
    return render(request, 'Admin/User details view.html')

def userssearch(request):
    from_date=request.POST['textfield']
    to_date=request.POST['textfield2']
    usrv=Request.objects.filter(date__range=[from_date,to_date])
    return render(request, 'Admin/view User request.html',{'dataus':usrv})


def userreqview(request):
    ur=Request.objects.filter(status="pending")
    return render(request,'Admin/view User request.html',{'dataus':ur})

def userreqview_post(request):
    from_date = request.POST['textfield']
    to_date = request.POST['textfield2']
    usrv = Request.objects.filter(date__range=[from_date, to_date])
    return render(request, 'Admin/view User request.html',{'dataus':usrv})

def reqaccept(request,id):
    Request.objects.filter(id=id).update(status="Approved")
    return HttpResponse("<script>alert('Candidate Accepted');window.location='/myapp/managecastingview/'</script>")

def rereject(request,id):
    Request.objects.filter(id=id).update(status="Rejected")
    return HttpResponse("<script>alert('Rejected');window.location='/myapp/userreqview/'</script>")


def searchuserall(request):
    To_age=request.POST['textfield98']
    from_age=request.POST['textfield89']
    objvu=Registeration.objects.filter(age__gte=from_age,age__lte=To_age)
    return render(request, 'Admin/view user-6.html',{'data':objvu})
def viewuser(request):
    objvu=Registeration.objects.all()
    return render(request,'Admin/view user-6.html',{'data':objvu})
def viewuser_post(request):
    obj5=request.objects.all()
    return render(request, 'Admin/view user-6.html',{'data5':obj5})





#############################################3


def userhome(request):
    return render(request,'user/USER HOME.html')


def achievementsadd(request):
    return render(request, 'user/achievements add.html')
def achievementsadd_post(request):
    achievements=request.POST['textarea']
    certificate=request.FILES['fileField']
    experience=request.POST['textfield']


    fs1 = FileSystemStorage()
    date1 = datetime.datetime.now().strftime('%Y%m%d-%H%M%S') + '.jpg'
    fs1.save(date1,certificate)
    path2 = fs1.url(date1)


    aobj=Achievement()
    aobj.date=datetime.datetime.now().strftime("%Y-%m-%d")
    aobj.achievements=achievements
    aobj.certificates=path2
    aobj.experience=experience
    aobj.USER=Registeration.objects.get(LOGIN_id=request.session['lid'])
    aobj.save()

    return HttpResponse("<script>alert('Achievements Added');window.location='/myapp/achievementview/'</script>")


def achievementview(request):
    obj7=Achievement.objects.all()
    return render(request, 'user/achievement view.html',{'data7':obj7})
def achievementview_post(request):
    return render(request, 'user/achievement view.html')


def achievementsedit(request,id):
    obj=Achievement.objects.get(id=id)
    return render(request,'user/achievements edit.html',{"data":obj})

def achievementsedit_post(request,id):
    achievements = request.POST['textarea']
    experience = request.POST['textarea2']
    id=id

    if 'fileField' in request.FILES:

        certificate = request.FILES['fileField']
        fs1 = FileSystemStorage()
        date1 = datetime.datetime.now().strftime('%Y%m%d-%H%M%S') + '.jpg'
        fs1.save(date1, certificate)
        path2 = fs1.url(date1)
        Achievement.objects.filter(id=id).update(certificates=path2)

    date = datetime.datetime.now().strftime("%Y-%m-%d")
    Achievement.objects.filter(id=id).update(date=date,achievements=achievements,experience=experience)
    return HttpResponse("<script>alert('Updated Successfully');window.location='/myapp/achievementview/'</script>")


def approvesearch(request):
    casting_film=request.POST['textfield']
    objv = Request.objects.filter(status='Approved',CASTING__casting_film__contains=casting_film)
    return render(request, 'user/Approval formuse.html',{'data':objv})
def approvalformuse(request):
    s=Selectedcandidates.objects.filter(REQUEST__USER__LOGIN_id= request.session['lid'])
    return render(request, 'user/Approval formuse.html',{'data':s})
def approvalformuse_post(request):
    obj8=request.objects.all()
    return render(request, 'user/Approval formuse.html',{'data8':obj8})

def apaccept(request,id):
    Selectedcandidates.objects.filter(id=id).update(status="approved")
    return HttpResponse("<script>alert('Accepted');window.location='/myapp/approvalformuse/'</script>")
def apreject(request,id):
    Selectedcandidates.objects.filter(id=id).update(status="Rejected")
    return HttpResponse("<script>alert('Rejected');window.location='/myapp/approvalformuse/'</script>")



def castingsearch(request):
    casting_film=request.POST['textfield']
    objcs=Managecastingsub.objects.filter(MANAGECASTINGMAIN__casting_film__icontains=casting_film)
    return render(request, 'user/CASTING INFO VIEW-22.html',{'data9':objcs})
def castinginfoview(request):
    objcs=Managecastingsub.objects.all()
    return render(request,'user/CASTING INFO VIEW-22.html',{'data9':objcs})
def castinginfoview_post(request):
    obj9=Managecastingsub.objects.all()
    return render(request,'user/CASTING INFO VIEW-22.html',{'data9':obj9})


def complaintsend(request,id):
    return render(request,'user/complaint -send.html',{'id':id})

def complaintsend_post(request):
    complaint=request.POST['textarea']
    id=request.POST['id']

    cmobj=Complaint()
    cmobj.complaint=complaint
    cmobj.date=datetime.datetime.now().today()
    cmobj.reply="pending"
    cmobj.status="pending"
    cmobj.USER=Registeration.objects.get(LOGIN_id=request.session['lid'])
    cmobj.CASTING=Managecastingmain.objects.get(id=id)
    cmobj.save()
    return HttpResponse("<script>alert('Sending Complaint');window.location='/myapp/complaintviewreply/'</script>")

def complaintsearch(request):
    from_date = request.POST['textfield']
    to_date = request.POST['textfield2']
    csd=Complaint.objects.filter(date__range=[from_date,to_date])
    return render(request,'user/complaint -view reply.html',{'data10':csd})
def complaintviewreply(request):
    cr=Complaint.objects.filter(USER__LOGIN_id=request.session['lid'])
    return render(request,'user/complaint -view reply.html',{'data10':cr})
def complaintviewreply_post(request):
    obj10=request.objects.all()
    return render(request,'user/complaint -view reply.html',{'data10':obj10})

def emailview(request):
    return render(request,'user/emailview.html')
def emailview_post(request):
    obj11=request.objects.all()
    return render(request,'user/emailview.html',{'data11':obj11})

def registrationformadd(request):
    return render(request, 'user/Registration form-18.html')

def registrationform_post(request):
    name=request.POST['textfield']
    contact=request.POST['textfield3']
    email=request.POST['textfield2']
    dob=request.POST['textfield4']
    photo=request.FILES['textfield141']
    age=request.POST['textfield5']
    gender=request.POST['RadioGroup1']
    street=request.POST['textfield6']
    place=request.POST['textfield7']
    post=request.POST['textfield8']
    district=request.POST['textfield9']
    state=request.POST['textfield10']

    pincode=request.POST['textfield11']
    height=request.POST['textfield12']
    weight=request.POST['textfield13']
    instagramid=request.POST['textfield33']
    cv=request.FILES['fileField']
    password=request.POST['textfield131']
    confirm_password=request.POST['textfield132']

    fs = FileSystemStorage()
    date = datetime.datetime.now().strftime('%Y%m%d-%H%M%S') + '.jpg'

    fs.save(date,photo)
    path=fs.url(date)

    fs1 = FileSystemStorage()
    date1 = datetime.datetime.now().strftime('%Y%m%d-%H%M%S') + 'cv.pdf'
    fs1.save(date1, cv)
    path2 = fs1.url(date1)

    lobj=Login()
    lobj.usename=email
    lobj.passwod= password
    lobj.type = 'user'
    lobj.save()

    robj=Registeration()
    if password == confirm_password:
        robj.name=name
        robj.email=email
        robj.contact=contact
        robj.dob=dob
        robj.photo=path
        robj.age=age
        robj.gender=gender
        robj.street=street
        robj.place=place
        robj.post=post
        robj.post=district
        robj.district=district
        robj.state=state
        robj.pincode=pincode
        robj.height=height
        robj.weight=weight
        robj.instagramid=instagramid
        robj.cv=path2
        robj.LOGIN=lobj
        robj.save()
        return HttpResponse("<script>alert('Registeration Succesfull');window.location='/myapp/login/'</script>")
    else:
        return HttpResponse("<script>alert('invalid');window.location='/myapp/login/'</script>")



def registrationformview(request):
    obj12 = Registeration.objects.get(LOGIN_id=request.session['lid'])
    return render(request, 'user/Registration form-view.html', {'data':obj12})

def registerationedit(request,id):
    obj20=Registeration.objects.get(id=id)
    return render(request, 'user/Registration form-edit.html', {'data':obj20})

def registrationedit_post(request):
    id=request.POST['id']
    name = request.POST['textfield']
    contact = request.POST['textfield3']
    email = request.POST['textfield2']
    dob = request.POST['textfield4']

    age = request.POST['textfield5']
    gender = request.POST['RadioGroup1']
    street = request.POST['textfield6']
    place = request.POST['textfield7']
    post = request.POST['textfield8']
    district = request.POST['textfield9']
    state = request.POST['textfield10']
    fs = FileSystemStorage()
    date = datetime.datetime.now().strftime('%Y%m%d-%H%M%S') + '.jpg'
    pincode = request.POST['textfield11']
    height = request.POST['textfield12']
    weight = request.POST['textfield13']
    instagramid = request.POST['textfield33']


    robj = Registeration.objects.get(id=id)

    if 'photo' and 'cv' in request.FILES:
        cv = request.FILES['fileField']
        photo = request.FILES['textfield14']


        fs.save(date, photo)
        path = fs.url(date)

        fs1 = FileSystemStorage()
        date1 = datetime.datetime.now().strftime('%Y%m%d-%H%M%S') + 'cv.pdf'
        fs1.save(date1, cv)
        path2 = fs1.url(date1)
        robj.photo = path
        robj.cv = path2
        robj.save()

    robj.name = name
    robj.email = email
    robj.contact = contact
    robj.dob = dob
    robj.age = age
    robj.gender = gender
    robj.street = street
    robj.place = place
    robj.post = post
    robj.post = district
    robj.district = district
    robj.state = state
    robj.pincode = pincode
    robj.height = height
    robj.weight = weight
    robj.instagramid = instagramid
    robj.save()
    return HttpResponse("<script>alert('edited');window.location='/myapp/registrationformview/'</script>")


def requestform(request,id):
    return render(request, 'user/request form .html',{"id":id})

def requestform_post(request):
    id=request.POST['id']
    vid=request.FILES['fileField']
    fs=FileSystemStorage()
    d=datetime.datetime.now().strftime('%Y%m%d%H%M%S')+'.mp3'
    fs.save(d,vid)
    path=fs.url(d)


    if Request.objects.filter(CASTING_id=id):
        return HttpResponse("<script>alert('Already Requested');window.location='/myapp/userhome/'</script>")

    objr=Request()
    objr.video=path
    objr.date=datetime.datetime.today()
    objr.status='pending'
    objr.CASTING_id=id
    objr.USER=Registeration.objects.get(LOGIN_id=request.session['lid'])
    objr.save()
    return HttpResponse("<script>alert('Requesting Succesfull');window.location='/myapp/userhome/'</script>")

def requeststatus(request):
    res=Request.objects.filter(USER__LOGIN__id=request.session['lid'])
    return render(request, 'user/request status.html',{'data':res})
def requeststatus_post(request):
    obj13=request.objects.all()
    return render(request, 'user/request status.html',{'data13':obj13})


def reviewsend(request):
    return render(request, 'user/send review.html',)
def reviewsend_post(request):
    review=request.POST['textarea']
    rating=request.POST['textfield']
    rvs=Review()
    rvs.date=datetime.datetime.now().today()
    rvs.review=review
    rvs.rating=rating
    rvs.USER = Registeration.objects.get(LOGIN=request.session['lid'])
    rvs.save()

    return HttpResponse("<script>alert('Sending Review');window.location='/myapp/reviewviewuser'</script>")

def reviewviewuser(request):
    obj14=Review.objects.filter(USER__LOGIN_id=request.session['lid'])
    return render(request, 'user/review view.html',{'data':obj14})
def reviewviewuser_post(request):
    return render(request, 'user/review view.html')


def changepsus(request):
    return render(request, 'user/Change Password.html')
def changepsus_post(request):
    current_password=request.POST['textfield']
    new_password=request.POST['textfield2']
    confirm_password=request.POST['textfield3']
    cobj=Login.objects.filter(id=request.session['lid'],passwod=current_password)
    if cobj.exists():
        cobj2=Login.objects.get(id=request.session['lid'],passwod=current_password)
        if new_password==confirm_password:
            cobj3=Login.objects.filter(id=request.session['lid']).update(passwod=confirm_password)
            return HttpResponse("<script>alert('successfully changed');window.location='/myapp/login/'</script>")
        else:
            return HttpResponse("<script>alert('password missmatch');window.location='/myapp/changepsus/'</script>")
    else:
        return HttpResponse("<script>alert('please check current password');window.location='/myapp/changepsus/'</script>")


def respectivecastinginfoview(request,id):
    rci=Selectedcandidates.objects.get(id=id)


    rs= Managecastingsub.objects.get(MANAGECASTINGMAIN=rci.REQUEST.CASTING)
    return render(request,'user/respectivecastview.html',{'data':rci,'rs':rs})

def respectivecastinginfoview_post(request):
    return render(request,'user/respectivecastview.html')






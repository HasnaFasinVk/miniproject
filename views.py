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


def adminhome(request):
    return render(request,'Admin/ADMIN HOME.html')

def forgotps(request):
    return render(request,'forgot ps.html')
def forgotps_post(request):
    forgot_password=request.POST['textfield']
    email=request.POST['textfield']
    return render(request,'forgot ps.html')

def changeps(request):
    return render(request, 'Admin/Change Password.html')
def changeps_post(request):
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
            return HttpResponse("<script>alert('password missmatch');window.location='/myapp/changeps/'</script>")
    else:
        return HttpResponse("<script>alert('please check current password');window.location='/myapp/changeps/'</script>")




def approvalform(request):
    return render(request,'Admin/Approval Formad.html')

def approvalform_post(request):
    presciption=request.POST['textfield']
    meeting_date=request.POST['textfield6']
    venue=request.POST['textfield5']
    time=request.POST['textfield4']
    contact=request.POST['textfield3']
    obja=Selectedcandidates()
    obja.prescription=presciption
    obja.date=datetime.datetime.now().strftime("%Y-%m-%d")
    obja.meeting_date=meeting_date
    obja.venue=venue
    obja.time=time
    obja.contact=contact
    return HttpResponse("<script>alert('shared successfully');window.location='/myapp/approvalform/'</script>")

def approvalformviewad(request):
    return render(request,'Admin/Approval Form view.html')
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
    return HttpResponse("<script>alert('replied');window.loction=/myapp/complaintview/</script>")

def complaint_search(request):
    from_date=request.POST['textfield']
    to_date=request.POST['textfield2']

    crobj=Complaint.objects.filter(date__range=[from_date,to_date])
    return render(request,'Admin/Complaint-view.html',{'data':crobj})

def complaintview(request):
    cv=Complaint.objects.all()
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
    objms.save()
    return HttpResponse("<script>alert('casting added succesfully');window.location='/myapp/managecastadd/'</script>")

def managecastedit(request):
    return render(request,'Admin/manage casting-edit.html')
def managecastedit_post(request):
    film_name = request.POST['textfield7']
    casting_manager = request.POST['textfield6']
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
    return render(request, 'Admin/manage casting-edit.html')

def filmsearch(request):
    casting_film=request.POST['textfield']
    return render(request, 'Admin/manage casting-view.html')
def managecastingview(request):
    return render(request,'Admin/manage casting-view.html')
def managecastingview_post(request):
    obj=Managecastingsub.objects.all()
    return render(request, 'Admin/manage casting-view.html',{"data":obj})


def reviewsearch(request):
    from_fate=request.POST['textfield']
    to_date=request.POST['textfield2']
    return render(request,'Admin/Review view.html')
def reviewview(request):
    return render(request,'Admin/Review view.html')
def reviewview_post(request):
    obj6=Review.objects.all()
    return render(request, 'Admin/Review view.html',{'data6':obj6})

def selecandidatesearch(request):
    from_date=request.POST['textfield']
    to_date=request.POST['textfield2']
    return render(request, 'Admin/Selected candidates VIEW.html')
def selectedcandidates(request):
    return render(request,'Admin/Selected candidates VIEW.html')
def selectedcandidates_post(request):
    obj1=selectedcandidates.objects.all()
    return render(request, 'Admin/Selected candidates VIEW.html',{'data1':obj1})

def userdetailview(request):
    return render(request,'Admin/User details view.html')
def userdetailview_post(request):
    obj2=Registeration.objects.all()
    obj3=Achievement.objects.all()
    return render(request, 'Admin/User details view.html',{'data2':obj2},{'data3':obj3})

def userssearch(request):
    from_date=request.POST['textfield']
    to_date=request.POST['textfield2']
    return render(request, 'Admin/view User request.html')
def userreqview(request):
    return render(request,'Admin/view User request.html')
def userreqview_post(request):
    obj4= request.objects.all()
    return render(request, 'Admin/view User request.html',{'data4':obj4})


def searchuserall(request):
    age=request.POST['textfield']
    return render(request, 'Admin/view user-6.html')
def viewuser(request):
    return render(request,'Admin/view user-6.html')
def viewuser_post(request):
    obj5=request.objects.all()
    return render(request, 'Admin/view user-6.html',{'data5':obj5})





#############################################3


def userhome(request):
    return render(request,'user/USER HOME.html')

def achievementview(request):
    return render(request, 'user/achievement view.html')
def achievementview_post(request):
    obj7=request.objects.all()
    return render(request, 'user/achievement view.html',{'data7':obj7})

def achievementsadd(request):
    return render(request, 'user/achievements add.html')
def achievementsadd_post(request):
    achievements=request.POST['textarea']
    certificate=request.FILES['fileField']
    experience=request.POST['textfield']
    instagram_id=request.POST['textfield2']
    aobj=Achievement()
    aobj.date=datetime.datetime.now().strftime("%Y-%m-%d")
    aobj.achievements=achievements
    aobj.certificates=certificate
    aobj.experience=experience
    aobj.instagram_id=instagram_id

    fs1 = FileSystemStorage()
    date1 = datetime.datetime.now().strftime('%Y%m%d-%H%M%S') + '.jpg'
    fs1.save(date1,certificate)
    path2 = fs1.url(date1)
    return HttpResponse("<script>alert('Achievements Added');window.location='/myapp/achievementsadd/'</script>")



    return render(request, 'user/achievements add.html')

def achievementsedit(request):
    return render(request, 'user/achievements edit.html')
def achievementsedit_post(request):
    achievements = request.POST['textarea']
    certificate = request.POST['fileField']
    experience = request.POST['textarea2']
    instagram_id=request.POST['textfield']
    return render(request, 'user/achievements edit.html')

def approvesearch(request):
    casting_film=request.POST['textfield']
    return render(request, 'user/Approval formuse.html')
def approvalformuse(request):
    return render(request, 'user/Approval formuse.html')
def approvalformuse_post(request):
    obj8=request.objects.all()
    return render(request, 'user/Approval formuse.html',{'data8':obj8})


def castingsearch(request):
    casting_film=request.POST['textfield']
    return render(request, 'user/CASTING INFO VIEW-22.html')
def castinginfoview(request):
    return render(request,'user/CASTING INFO VIEW-22.html')
def castinginfoview_post(request):
    obj9=request.objects.all()
    return render(request,'user/CASTING INFO VIEW-22.html',{'data9':obj9})

def changepsuser(request):
    return render(request, 'user/Change Password.html')
def changepsuser_post(request):
    current_password=request.POST['textfield']
    new_password = request.POST['textfield2']
    confirm_password = request.POST['textfield3']
    return render(request, 'user/Change Password.html')

def complaintsend(request):
    return render(request,'user/complaint -send.html')
def complaintsend_post(request):
    complaint=request.POST['textarea']
    return render(request,'user/complaint -send.html')

def complaintsearch(request):
    from_date = request.POST['textfield']
    to_date = request.POST['textfield2']
    return render(request,'user/complaint -view reply.html')
def complaintviewreply(request):
    return render(request,'user/complaint -view reply.html')
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
    fs=FileSystemStorage()
    date=datetime.datetime.now().strftime('%Y%m%d-%H%M%S')+'.jpg'
    pincode=request.POST['textfield11']
    height=request.POST['textfield12']
    weight=request.POST['textfield13']
    cv=request.FILES['fileField']
    password=request.POST['textfield131']
    confirm_password=request.POST['textfield132']

    fs.save(date,photo)
    path=fs.url(date)

    fs1 = FileSystemStorage()
    date1 = datetime.datetime.now().strftime('%Y%m%d-%H%M%S') + 'cv.jpg'
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


    robj = Registeration.objects.get(id=id)

    if 'photo' and 'cv' in request.FILES:
        cv = request.FILES['fileField']
        photo = request.FILES['textfield14']


        fs.save(date, photo)
        path = fs.url(date)

        fs1 = FileSystemStorage()
        date1 = datetime.datetime.now().strftime('%Y%m%d-%H%M%S') + 'cv.jpg'
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
    robj.save()
    return HttpResponse("<script>alert('edited');window.location='/myapp/registrationformview/'</script>")


def requestform(request):
    return render(request, 'user/request form .html')
def requestform_post(request):
    video=request.POST['fileField']
    return render(request, 'user/request form .html')

def requeststatus(request):
    return render(request, 'user/request status.html')
def requeststatus_post(request):
    obj13=request.objects.all()
    return render(request, 'user/request status.html',{'data13':obj13})

def reviewviewuser(request):
    return render(request, 'user/review view.html')
def reviewviewuser_post(request):
    obj14=request.objects.all()
    return render(request, 'user/review view.html',{'data14':obj14})

def reviewsend(request):
    return render(request, 'user/send review.html')
def reviewsend_post(request):
    review=request.POST['textarea']
    rating=request.POST['textfield']
    return render(request, 'user/send review.html')


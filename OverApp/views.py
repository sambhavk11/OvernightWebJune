from __future__ import unicode_literals
from django.shortcuts import render
import json
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib.auth import authenticate,login,logout
import django
import models
from django.core.mail import EmailMultiAlternatives




# Create your views here.
def landing_page(request):
    return render(request, 'landingpage.html')

def merchantSignup(request):
    return render(request,'merchantSignup.html')

def loadMerchantLogin(request):
    return render(request,'merchantLogin.html')
def loadDash(request):
    roomdata = models.Roominfo.objects.all().values()
    print "before max"
    getMax()
    print "After max "
    print roomdata
    return render(request,'hotelDashboard.html',{'roomdata':roomdata})

# api call to alchemy to get content
def get_content(request):
    print "here"
    res = ''
    if request.method == 'POST':
        params = request.POST
        val = params.get('search_keyword')
        print val

        print "outside"
    # return HttpResponse(json.dumps({'data': res}), content_type="application/json")
    return render(request, 'landingpage.html', {'data': res})
def showSearchresult(request):
    city=request.GET['searchbar']
    print city
    hoteldata=models.HotelInfo.objects.filter(Destination=city).values()
    return render(request,'searchresults_bali.html',{'data':hoteldata})

def showSearchresultJakarta(request):
    return render(request, 'searchresults_jakarta.html')

def uploadPage(request):
    return render(request,'uploadPics.html')



def loginUser (request):
    return render(request,'login.html')


def signup (request):
    return render(request,'signup.html')

def manageContent(request):
    return render(request,'manageContent.html')

def showBookingPage(request):
    return render(request, 'bookingdetails.html')

def showBookingConfirmation(request):
    return render(request, 'bookingconfirmation.html')

def showUserProfile(request):
    return render(request, 'user-profile.html')

def showUserProfileBookingHistory(request):
    return render(request, 'user-profile-booking-history.html')

def showUserProfileCards(request):
    return render(request, 'user-profile-cards.html')

def showUserProfileSettings(request):
    return render(request, 'user-profile-settings.html')

def updateRoomInfo(request):
    if request.method == 'POST':
        params = request.POST
        print params
        roomType=params.get("roomType")
        date=params.get("start")
        transport=params.get("transport")
        price=params.get("price")
        discount=params.get('discount')
        destination=params.get("destination")
        roomobj=models.Roominfo(Destination=destination,roomType=roomType,date=date,transport=transport,ratePerNight=price,discountPercent=discount)
        roomobj.save()

    roomdata = models.Roominfo.objects.all().values()
    return render(request, 'hotelDashboard.html', {'roomdata': roomdata})

def managePackage(request):
    roomdata = models.Roominfo.objects.all().values('roomType')
    return render(request,"managePackage.html",{'data':roomdata})

def createPackage(request):
    if request.method=='POST':
        name=request.POST['name']
        packagedesc=request.POST['packagedesc']
        price=request.POST['price']
        services=request.POST['services']
        roomType=request.POST['roomType']

        package=models.Package(packagename=name,packagedesc=packagedesc,price=price,roomType=roomType,serviceList=services)
        package.save()
        packageResponse=managePackage(request)

        return packageResponse


def createRoom(request):
    request_context = RequestContext(request)
    if request.method=='POST':
        destination = request.POST['destination']
        name = request.POST['name']
        address = request.POST['address']
        amenities = request.POST['amenities']
        services = request.POST['services']
        roomtypes=request.POST['roomtype']
        maxindex = getMax()+1
        print maxindex
        hotelId=destination+"-"+str(maxindex)
        roomarr=roomtypes.split(",")
        username=request.user
        print username
        for each in roomarr:
            room=models.Roominfo(HotelName=name,date='2016-01-01',ownerId=request.user,roomType=each.upper(),Destination=destination,ratePerNight=0.0,packagePrice=0.0,discountPercent=0.0,transport=0.0)
            room.save()

        hotel=models.HotelInfo(HotelID=hotelId,Destination=destination,HotelName=name,HotelAddress=address,HotelAmens=amenities,HotelServices=services)
        hotel.save()
        request.session['sess_hotelId']=hotelId
    return render(request,'uploadPics.html',{"data":hotelId})
    # return HttpResponse(destination+name+address+amenities+services+maxindex)


def uploadPics(request):
    hotelId=request.session['sess_hotelId']
    hotel=models.HotelInfo.objects.get(HotelID=hotelId)
    hotel.HotelPictures=request.FILES['hotelImage']
    hotel.save()
    roomdata = models.Roominfo.objects.filter(ownerId=request.user).values()
    return render(request, "hotelDashboard.html", {'roomdata': roomdata})


def createMerchant(request):
    request_context = RequestContext(request)
    if request.method=='POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        repass = request.POST['repass']
        if repass==password:
            user = User.objects.create_user(username=email,email=email,password=password)
            user.first_name=fname
            user.last_name=lname
            user.save()
            # modUser=django.contrib.auth.models.AuthUser.objects.get(email=email)
            # modUser.first_name=fname
            # modUser.last_name=lname
            # modUser.save()
            if user is None:
                return HttpResponse("Merchant Cannot be created")
            subject, from_email, to = 'Welcome to Overnight', 'overnightjunedep@gmail.com', email
            text_content = 'Hello!! '+ fname+"\n We Welcome You to Overnight"
            html_content = '<p>Hello '+ fname+'<br> We Welcome you to <strong>Overnight</strong> .</p>'
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            return render(request,'merchantLogin.html')
        return render(request,"merchantSignup.html",{"data":"Passwords do not match"})

def logonMerchant(request):
    request_cotext=RequestContext(request)
    if request.method=='POST':
        email = request.POST.get('email', False)
        password = request.POST.get('password', False)
        user = authenticate(username=email, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                print request.user
                roomdata=models.Roominfo.objects.filter(ownerId=user).values()
                return render(request,"hotelDashboard.html",{'roomdata':roomdata})
            return HttpResponse("User is not active")
        return HttpResponse("Invalid User")

def getMax():
    idarr=[]
    allIds=models.HotelInfo.objects.all().order_by("HotelID").values("HotelID")
    for each in allIds:
        idarr.append(int(each['HotelID'].split("-")[1]))
    return max(idarr)

# def jsonify(val,type):
#     initstr='['
#     valarr=val.split(",")
#     for each in valarr:

def logout_user(request):
    logout(request)
    return render(request,"landingpage.html")
